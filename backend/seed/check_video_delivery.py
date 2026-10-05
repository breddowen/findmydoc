# ./backend/seed/check_video_delivery.py
# python -m seed.check_video_delivery


import getpass
import http.cookiejar
import json
import urllib.error
import urllib.request
import uuid


def main() -> None:
    base = input(
        "API base [http://localhost:8000]: "
    ).strip() or "http://localhost:8000"

    base = base.rstrip("/")

    token = getpass.getpass("Access token: ").strip()
    video_id = str(uuid.UUID(input("Video ID: ").strip()))

    cookies = http.cookiejar.CookieJar()

    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cookies)
    )

    auth_headers = {
        "Authorization": f"Bearer {token}",
    }

    metadata_request = urllib.request.Request(
        f"{base}/api/v1/videos/{video_id}",
        headers=auth_headers,
    )

    with opener.open(metadata_request, timeout=15) as response:
        video = json.load(response)

    file = video.get("wide_file") or video.get("mobile_file")

    if not file:
        raise RuntimeError("У видео нет файла")

    file_url = (
        f"{base}/api/v1/videos/{video_id}"
        f"/files/{file['id']}"
    )

    # Без cookie доступ должен быть закрыт,
    # даже если URL файла известен.
    try:
        with urllib.request.urlopen(
            file_url,
            timeout=15,
        ):
            raise AssertionError(
                "Файл неожиданно доступен без медиасессии"
            )
    except urllib.error.HTTPError as error:
        assert error.code == 401, error.code
        print("OK: anonymous request -> 401")

    session_request = urllib.request.Request(
        f"{base}/api/v1/videos/media-session",
        data=b"",
        headers=auth_headers,
        method="POST",
    )

    with opener.open(session_request, timeout=15) as response:
        media_session = json.load(response)

    print(
        "Media session expires:",
        media_session["expires_at"],
    )

    range_request = urllib.request.Request(
        file_url,
        headers={
            "Range": "bytes=0-1023",
        },
    )

    with opener.open(range_request, timeout=15) as response:
        status = response.status
        content_range = response.headers.get("Content-Range")
        data = response.read(1025)

    assert status == 206, status
    assert content_range, "Missing Content-Range"
    assert len(data) == 1024, len(data)

    print("OK: partial request -> 206")
    print("Content-Range:", content_range)

    head_request = urllib.request.Request(
        file_url,
        method="HEAD",
    )

    with opener.open(head_request, timeout=15) as response:
        assert response.status == 200
        assert response.read() == b""

    print("OK: HEAD -> 200 without body")

    revoke_request = urllib.request.Request(
        f"{base}/api/v1/videos/media-session",
        method="DELETE",
    )

    with opener.open(revoke_request, timeout=15) as response:
        assert response.status == 204

    try:
        with opener.open(file_url, timeout=15):
            raise AssertionError(
                "Файл доступен после удаления медиасессии"
            )
    except urllib.error.HTTPError as error:
        assert error.code == 401, error.code

    print("OK: revoked session -> 401")
    print("Video delivery checks passed.")


if __name__ == "__main__":
    main()