у меня проблема: проект не деплоится через github actions

2026-08-30T18:02:20.5345715Z Current runner version: '2.336.0'
2026-08-30T18:02:20.5380950Z ##[group]Runner Image Provisioner
2026-08-30T18:02:20.5382694Z Hosted Compute Agent
2026-08-30T18:02:20.5384055Z Version: 20260819.586
2026-08-30T18:02:20.5385759Z Commit: 3cc4a88dfa507ef76119ad1bb3eccc6378bb2b76
2026-08-30T18:02:20.5387377Z Build Date: 2026-08-18T23:20:18Z
2026-08-30T18:02:20.5388812Z Worker ID: {9a5fe558-cc7d-4e6f-8d4e-4ec631723b4d}
2026-08-30T18:02:20.5390423Z Azure Region: eastus
2026-08-30T18:02:20.5391647Z ##[endgroup]
2026-08-30T18:02:20.5395031Z ##[group]Operating System
2026-08-30T18:02:20.5396361Z Ubuntu
2026-08-30T18:02:20.5397697Z 24.04.4
2026-08-30T18:02:20.5398879Z LTS
2026-08-30T18:02:20.5400043Z ##[endgroup]
2026-08-30T18:02:20.5401327Z ##[group]Runner Image
2026-08-30T18:02:20.5402704Z Image: ubuntu-24.04
2026-08-30T18:02:20.5404037Z Version: 20260823.283.1
2026-08-30T18:02:20.5406732Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260823.283/images/ubuntu/Ubuntu2404-Readme.md
2026-08-30T18:02:20.5409810Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260823.283
2026-08-30T18:02:20.5411808Z ##[endgroup]
2026-08-30T18:02:20.5414508Z ##[group]GITHUB_TOKEN Permissions
2026-08-30T18:02:20.5417741Z Contents: read
2026-08-30T18:02:20.5419018Z Metadata: read
2026-08-30T18:02:20.5420193Z Packages: write
2026-08-30T18:02:20.5421534Z ##[endgroup]
2026-08-30T18:02:20.5425010Z Secret source: Actions
2026-08-30T18:02:20.5427511Z Prepare workflow directory
2026-08-30T18:02:20.5895611Z Prepare all required actions
2026-08-30T18:02:20.5965924Z Getting action download info
2026-08-30T18:02:20.7660612Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-08-30T18:02:20.9954927Z Complete job name: Deploy
2026-08-30T18:02:21.0731676Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-08-30T18:02:21.0740812Z ##[group]Run actions/checkout@v4
2026-08-30T18:02:21.0741680Z with:
2026-08-30T18:02:21.0742248Z   repository: breddowen/findmydoc
2026-08-30T18:02:21.0746550Z   token: ***
2026-08-30T18:02:21.0747117Z   ssh-strict: true
2026-08-30T18:02:21.0747676Z   ssh-user: git
2026-08-30T18:02:21.0748246Z   persist-credentials: true
2026-08-30T18:02:21.0748855Z   clean: true
2026-08-30T18:02:21.0749441Z   sparse-checkout-cone-mode: true
2026-08-30T18:02:21.0750080Z   fetch-depth: 1
2026-08-30T18:02:21.0750634Z   fetch-tags: false
2026-08-30T18:02:21.0751216Z   show-progress: true
2026-08-30T18:02:21.0751796Z   lfs: false
2026-08-30T18:02:21.0752369Z   submodules: false
2026-08-30T18:02:21.0752946Z   set-safe-directory: true
2026-08-30T18:02:21.0753581Z   allow-unsafe-pr-checkout: false
2026-08-30T18:02:21.0754759Z ##[endgroup]
2026-08-30T18:02:21.1796737Z Syncing repository: breddowen/findmydoc
2026-08-30T18:02:21.1799608Z ##[group]Getting Git version info
2026-08-30T18:02:21.1800984Z Working directory is '/home/runner/work/findmydoc/findmydoc'
2026-08-30T18:02:21.1803019Z [command]/usr/bin/git version
2026-08-30T18:02:21.2022400Z git version 2.55.0
2026-08-30T18:02:21.2065744Z ##[endgroup]
2026-08-30T18:02:21.2086057Z Temporarily overriding HOME='/home/runner/work/_temp/504fba98-337c-4af7-8084-531c6280017f' before making global git config changes
2026-08-30T18:02:21.2088970Z Adding repository directory to the temporary git global config as a safe directory
2026-08-30T18:02:21.2091336Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/findmydoc/findmydoc
2026-08-30T18:02:21.2199285Z Deleting the contents of '/home/runner/work/findmydoc/findmydoc'
2026-08-30T18:02:21.2202125Z ##[group]Initializing the repository
2026-08-30T18:02:21.2203725Z [command]/usr/bin/git init /home/runner/work/findmydoc/findmydoc
2026-08-30T18:02:21.2298388Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-08-30T18:02:21.2300912Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-08-30T18:02:21.2303386Z hint: to use in all of your new repositories, which will suppress this warning,
2026-08-30T18:02:21.2306925Z hint: call:
2026-08-30T18:02:21.2308020Z hint:
2026-08-30T18:02:21.2309332Z hint: 	git config --global init.defaultBranch <name>
2026-08-30T18:02:21.2310741Z hint:
2026-08-30T18:02:21.2312085Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-08-30T18:02:21.2315479Z hint: 'development'. The just-created branch can be renamed via this command:
2026-08-30T18:02:21.2317390Z hint:
2026-08-30T18:02:21.2318467Z hint: 	git branch -m <name>
2026-08-30T18:02:21.2319676Z hint:
2026-08-30T18:02:21.2321136Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-08-30T18:02:21.2323457Z Initialized empty Git repository in /home/runner/work/findmydoc/findmydoc/.git/
2026-08-30T18:02:21.2327630Z [command]/usr/bin/git remote add origin https://github.com/breddowen/findmydoc
2026-08-30T18:02:21.2382972Z ##[endgroup]
2026-08-30T18:02:21.2384918Z ##[group]Disabling automatic garbage collection
2026-08-30T18:02:21.2386934Z [command]/usr/bin/git config --local gc.auto 0
2026-08-30T18:02:21.2475307Z ##[endgroup]
2026-08-30T18:02:21.2485774Z ##[group]Setting up auth
2026-08-30T18:02:21.2487526Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-08-30T18:02:21.2492286Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-08-30T18:02:21.2947358Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-08-30T18:02:21.2985637Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-08-30T18:02:21.3253985Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-08-30T18:02:21.3295734Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-08-30T18:02:21.3531624Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-08-30T18:02:21.3586267Z ##[endgroup]
2026-08-30T18:02:21.3593890Z ##[group]Fetching the repository
2026-08-30T18:02:21.3602112Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +6bc2ad6ec7bb1a2c236ed7ea9dd9b4cfc782b194:refs/remotes/origin/develop
2026-08-30T18:02:22.0031288Z From https://github.com/breddowen/findmydoc
2026-08-30T18:02:22.0034016Z  * [new ref]         6bc2ad6ec7bb1a2c236ed7ea9dd9b4cfc782b194 -> origin/develop
2026-08-30T18:02:22.0041269Z ##[endgroup]
2026-08-30T18:02:22.0044486Z ##[group]Determining the checkout info
2026-08-30T18:02:22.0047870Z ##[endgroup]
2026-08-30T18:02:22.0050024Z [command]/usr/bin/git sparse-checkout disable
2026-08-30T18:02:22.0105383Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-08-30T18:02:22.0139686Z ##[group]Checking out the ref
2026-08-30T18:02:22.0143872Z [command]/usr/bin/git checkout --progress --force -B develop refs/remotes/origin/develop
2026-08-30T18:02:22.3405488Z Switched to a new branch 'develop'
2026-08-30T18:02:22.3409333Z branch 'develop' set up to track 'origin/develop'.
2026-08-30T18:02:22.3421814Z ##[endgroup]
2026-08-30T18:02:22.3480815Z [command]/usr/bin/git log -1 --format=%H
2026-08-30T18:02:22.3510573Z 6bc2ad6ec7bb1a2c236ed7ea9dd9b4cfc782b194
2026-08-30T18:02:22.3745131Z ##[group]Run if [[ "${GITHUB_REF_NAME}" == "main" ]]; then
2026-08-30T18:02:22.3745769Z [36;1mif [[ "${GITHUB_REF_NAME}" == "main" ]]; then[0m
2026-08-30T18:02:22.3746259Z [36;1m  echo "name=production" >> "$GITHUB_OUTPUT"[0m
2026-08-30T18:02:22.3746966Z [36;1melif [[ "${GITHUB_REF_NAME}" == "develop" ]]; then[0m
2026-08-30T18:02:22.3747442Z [36;1m  echo "name=staging" >> "$GITHUB_OUTPUT"[0m
2026-08-30T18:02:22.3747841Z [36;1melse[0m
2026-08-30T18:02:22.3748340Z [36;1m  echo "Unsupported ***ment branch: ${GITHUB_REF_NAME}" >&2[0m
2026-08-30T18:02:22.3748814Z [36;1m  exit 1[0m
2026-08-30T18:02:22.3749133Z [36;1mfi[0m
2026-08-30T18:02:22.3791306Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-08-30T18:02:22.3791824Z ##[endgroup]
2026-08-30T18:02:22.4006705Z ##[group]Run mkdir -p ~/.ssh
2026-08-30T18:02:22.4007162Z [36;1mmkdir -p ~/.ssh[0m
2026-08-30T18:02:22.4007510Z [36;1mchmod 700 ~/.ssh[0m
2026-08-30T18:02:22.4007844Z [36;1m[0m
2026-08-30T18:02:22.4008250Z [36;1mprintf '%s\n' "$SSH_PRIVATE_KEY" > ~/.ssh/id_ed25519[0m
2026-08-30T18:02:22.4008760Z [36;1mchmod 600 ~/.ssh/id_ed25519[0m
2026-08-30T18:02:22.4009124Z [36;1m[0m
2026-08-30T18:02:22.4009490Z [36;1mprintf '%s\n' "$VPS_KNOWN_HOSTS" > ~/.ssh/known_hosts[0m
2026-08-30T18:02:22.4009965Z [36;1mchmod 600 ~/.ssh/known_hosts[0m
2026-08-30T18:02:22.4045484Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-08-30T18:02:22.4045954Z env:
2026-08-30T18:02:22.4048058Z   SSH_PRIVATE_KEY: ***
2026-08-30T18:02:22.4052681Z   VPS_KNOWN_HOSTS: 
***
2026-08-30T18:02:22.4053028Z ##[endgroup]
2026-08-30T18:02:22.4199255Z ##[group]Run rsync \
2026-08-30T18:02:22.4199646Z [36;1mrsync \[0m
2026-08-30T18:02:22.4199972Z [36;1m  --archive \[0m
2026-08-30T18:02:22.4200317Z [36;1m  --compress \[0m
2026-08-30T18:02:22.4200652Z [36;1m  --delete \[0m
2026-08-30T18:02:22.4201131Z [36;1m  -e "ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes -p ${VPS_PORT}" \[0m
2026-08-30T18:02:22.4201724Z [36;1m  ***/ \[0m
2026-08-30T18:02:22.4202124Z [36;1m  "${VPS_USER}@${VPS_HOST}:/opt/findmydoc/***/"[0m
2026-08-30T18:02:22.4236873Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-08-30T18:02:22.4237348Z env:
2026-08-30T18:02:22.4237738Z   VPS_HOST: ***
2026-08-30T18:02:22.4238062Z   VPS_PORT: ***
2026-08-30T18:02:22.4238385Z   VPS_USER: ***
2026-08-30T18:02:22.4238699Z ##[endgroup]
2026-08-30T18:02:23.8710007Z Permission denied, please try again.
2026-08-30T18:02:24.0212623Z Permission denied, please try again.
2026-08-30T18:02:24.1717498Z ***@***: Permission denied (publickey,password).
2026-08-30T18:02:24.1723128Z rsync: connection unexpectedly closed (0 bytes received so far) [sender]
2026-08-30T18:02:24.1723917Z rsync error: unexplained error (code 255) at io.c(232) [sender=3.2.7]
2026-08-30T18:02:24.1741060Z ##[error]Process completed with exit code 255.
2026-08-30T18:02:24.1891311Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-08-30T18:02:24.1893159Z Post job cleanup.
2026-08-30T18:02:24.2705477Z [command]/usr/bin/git version
2026-08-30T18:02:24.2746816Z git version 2.55.0
2026-08-30T18:02:24.2783943Z Temporarily overriding HOME='/home/runner/work/_temp/855f2527-07f4-4cbd-a038-cd20d1709605' before making global git config changes
2026-08-30T18:02:24.2785589Z Adding repository directory to the temporary git global config as a safe directory
2026-08-30T18:02:24.2790551Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/findmydoc/findmydoc
2026-08-30T18:02:24.2828051Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-08-30T18:02:24.2862258Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-08-30T18:02:24.3118964Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-08-30T18:02:24.3147684Z http.https://github.com/.extraheader
2026-08-30T18:02:24.3159641Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-08-30T18:02:24.3195835Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-08-30T18:02:24.3449035Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-08-30T18:02:24.3516423Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-08-30T18:02:24.3915796Z Cleaning up orphan processes
2026-08-30T18:02:24.4389373Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
на github в моем ремпозитории https://github.com/breddowen/findmydoc.git добавил:
Environments
You can configure environments with protection rules, variables, and secrets. Learn more about configuring environments.

staging 5 secrets
production 5 secrets

| Secret | Значение |
|---|---|
| `VPS_HOST` | IP или hostname VDS |
| `VPS_PORT` | `22` |
| `VPS_USER` | `deploy` |
| `VPS_SSH_PRIVATE_KEY` | содержимое приватного deployment-ключа | cat ~/.ssh/findmydoc_deploy_key
| `VPS_KNOWN_HOSTS` | запись SSH host key |

ключ генерил так:
ssh-keygen -t ed25519 -C "github-actions-findmydoc" -f ./findmydoc_deploy_key

PS F:\Soft\!Laptops\~~EMC_projects\COMMERCIAL\COMMERCIAL_PROJ_0> cat ./findmydoc_deploy_key.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJPSHn/ahrBwAW7Gy1JuaSdg6YJtrYV3nzBgfZbdRv4k github-actions-findmydoc

на удаленном сервере:
deploy@chkldksgji:~$ cat ~/.ssh/authorized_keys
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJPSHn/ahrBwAW7Gy1JuaSdg6YJtrYV3nzBgfZbdRv4k github-actions-findmydoc

почему выдает ошибку?

name: Build and deploy

on:
  push:
    branches:
      - main
      - develop

  workflow_dispatch:

permissions:
  contents: read
  packages: write

concurrency:
  group: findmydoc-vds-deployment
  cancel-in-progress: false

jobs:
  build:
    name: Build and publish images
    runs-on: ubuntu-24.04

    outputs:
      image_prefix: ${{ steps.names.outputs.image_prefix }}
      image_tag: ${{ steps.names.outputs.image_tag }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Prepare image names
        id: names
        shell: bash
        run: |
          REPOSITORY="$(echo '${{ github.repository }}' | tr '[:upper:]' '[:lower:]')"

          echo "image_prefix=ghcr.io/${REPOSITORY}" >> "$GITHUB_OUTPUT"
          echo "image_tag=${GITHUB_SHA}" >> "$GITHUB_OUTPUT"

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push backend
        uses: docker/build-push-action@v6
        with:
          context: .
          file: deploy/backend.Dockerfile
          push: true
          tags: |
            ${{ steps.names.outputs.image_prefix }}-backend:${{ steps.names.outputs.image_tag }}
            ${{ steps.names.outputs.image_prefix }}-backend:${{ github.ref_name }}
          cache-from: type=gha,scope=backend
          cache-to: type=gha,mode=max,scope=backend

      - name: Build and push frontend
        uses: docker/build-push-action@v6
        with:
          context: .
          file: deploy/frontend.Dockerfile
          push: true
          tags: |
            ${{ steps.names.outputs.image_prefix }}-frontend:${{ steps.names.outputs.image_tag }}
            ${{ steps.names.outputs.image_prefix }}-frontend:${{ github.ref_name }}
          cache-from: type=gha,scope=frontend
          cache-to: type=gha,mode=max,scope=frontend

  deploy:
    name: Deploy
    needs:
      - build

    runs-on: ubuntu-24.04

    environment:
      name: ${{ github.ref_name == 'main' && 'production' || 'staging' }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Determine target environment
        id: target
        shell: bash
        run: |
          if [[ "${GITHUB_REF_NAME}" == "main" ]]; then
            echo "name=production" >> "$GITHUB_OUTPUT"
          elif [[ "${GITHUB_REF_NAME}" == "develop" ]]; then
            echo "name=staging" >> "$GITHUB_OUTPUT"
          else
            echo "Unsupported deployment branch: ${GITHUB_REF_NAME}" >&2
            exit 1
          fi

      - name: Configure SSH
        shell: bash
        env:
          SSH_PRIVATE_KEY: ${{ secrets.VPS_SSH_PRIVATE_KEY }}
          VPS_KNOWN_HOSTS: ${{ secrets.VPS_KNOWN_HOSTS }}
        run: |
          mkdir -p ~/.ssh
          chmod 700 ~/.ssh

          printf '%s\n' "$SSH_PRIVATE_KEY" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519

          printf '%s\n' "$VPS_KNOWN_HOSTS" > ~/.ssh/known_hosts
          chmod 600 ~/.ssh/known_hosts

      - name: Upload deployment configuration
        shell: bash
        env:
          VPS_HOST: ${{ secrets.VPS_HOST }}
          VPS_PORT: ${{ secrets.VPS_PORT || '22' }}
          VPS_USER: ${{ secrets.VPS_USER }}
        run: |
          rsync \
            --archive \
            --compress \
            --delete \
            -e "ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes -p ${VPS_PORT}" \
            deploy/ \
            "${VPS_USER}@${VPS_HOST}:/opt/findmydoc/deploy/"

      - name: Run deployment 
        shell: bash
        env:
          VPS_HOST: ${{ secrets.VPS_HOST }} 
          VPS_PORT: ${{ secrets.VPS_PORT || '22' }}
          VPS_USER: ${{ secrets.VPS_USER }}
          TARGET: ${{ steps.target.outputs.name }}
          IMAGE_PREFIX: ${{ needs.build.outputs.image_prefix }}  
          IMAGE_TAG: ${{ needs.build.outputs.image_tag }}
        run: |
          ssh \
            -i ~/.ssh/id_ed25519 \
            -o IdentitiesOnly=yes \
            -p "${VPS_PORT}" \
            "${VPS_USER}@${VPS_HOST}" \
            "chmod +x /opt/findmydoc/deploy/scripts/*.sh && \
             /opt/findmydoc/deploy/scripts/deploy.sh \
             '${TARGET}' \
             '${IMAGE_PREFIX}' \
             '${IMAGE_TAG}'"
весь проект:
# Project Structure

> Generated: 2026-08-30 21:05

---

## AI Backend

```
backend/alembic/env.py
backend/alembic/README
backend/alembic/script.py.mako
backend/alembic/versions/4a9d77a6cc23_initial_schema.py
backend/app/.env
backend/app/__init__.py
backend/app/core/__init__.py
backend/app/core/config.py
backend/app/core/db.py
backend/app/core/email.py
backend/app/core/security.py
backend/app/core/websockets/__init__.py
backend/app/core/websockets/manager.py
backend/app/main.py
backend/app/modules/__init__.py
backend/app/modules/articles/__init__.py
backend/app/modules/articles/models.py
backend/app/modules/articles/routers.py
backend/app/modules/articles/schemas.py
backend/app/modules/articles/utils.py
backend/app/modules/assignments/__init__.py
backend/app/modules/assignments/enums.py
backend/app/modules/assignments/models.py
backend/app/modules/assignments/routers.py
backend/app/modules/assignments/schemas.py
backend/app/modules/assignments/utils.py
backend/app/modules/auth/__init__.py
backend/app/modules/auth/models.py
backend/app/modules/auth/routers.py
backend/app/modules/auth/schemas.py
backend/app/modules/auth/utils.py
backend/app/modules/consents/__init__.py
backend/app/modules/consents/enums.py
backend/app/modules/consents/models.py
backend/app/modules/consents/routers.py
backend/app/modules/consents/schemas.py
backend/app/modules/consents/utils.py
backend/app/modules/content/__init__.py
backend/app/modules/content/utils.py
backend/app/modules/events/__init__.py
backend/app/modules/events/enums.py
backend/app/modules/events/models.py
backend/app/modules/events/routers.py
backend/app/modules/events/schemas.py
backend/app/modules/events/service.py
backend/app/modules/invitations/__init__.py
backend/app/modules/invitations/enums.py
backend/app/modules/invitations/models.py
backend/app/modules/invitations/routers.py
backend/app/modules/invitations/schemas.py
backend/app/modules/invitations/utils.py
backend/app/modules/notifications/__init__.py
backend/app/modules/notifications/enums.py
backend/app/modules/notifications/models.py
backend/app/modules/notifications/routers.py
backend/app/modules/notifications/schemas.py
backend/app/modules/notifications/service.py
backend/app/modules/patients/__init__.py
backend/app/modules/patients/enums.py
backend/app/modules/patients/routers.py
backend/app/modules/patients/schemas.py
backend/app/modules/patients/utils.py
backend/app/modules/programs/__init__.py
backend/app/modules/programs/enums.py
backend/app/modules/programs/models.py
backend/app/modules/programs/Readme.md
backend/app/modules/programs/routers.py
backend/app/modules/programs/schemas.py
backend/app/modules/programs/utils.py
backend/app/modules/questionnaires/__init__.py
backend/app/modules/questionnaires/enums.py
backend/app/modules/questionnaires/json_q/audit.json
backend/app/modules/questionnaires/models.py
backend/app/modules/questionnaires/Readme.md
backend/app/modules/questionnaires/routers.py
backend/app/modules/questionnaires/schemas.py
backend/app/modules/questionnaires/utils.py
backend/app/modules/referrals/__init__.py
backend/app/modules/referrals/enums.py
backend/app/modules/referrals/models.py
backend/app/modules/referrals/routers.py
backend/app/modules/referrals/schemas.py
backend/app/modules/referrals/utils.py
backend/app/modules/relationships/__init__.py
backend/app/modules/relationships/routers.py
backend/app/modules/relationships/schemas.py
backend/app/modules/specialities/__init__.py
backend/app/modules/specialities/routers.py
backend/app/modules/specialities/schemas.py
backend/app/modules/tags/__init__.py
backend/app/modules/tags/enums.py
backend/app/modules/tags/models.py
backend/app/modules/tags/routers.py
backend/app/modules/tags/schemas.py
backend/app/modules/tags/utils.py
backend/app/modules/users/__init__.py
backend/app/modules/users/enums.py
backend/app/modules/users/models.py
backend/app/modules/users/routers.py
backend/app/modules/users/schemas.py
backend/app/modules/users/utils.py
backend/requirements.txt
backend/seed/data/tags.json
backend/seed/data/users.json
backend/seed/Readme.md
backend/seed/upload_tags.py
backend/seed/upload_users.py
backend/test_database.db
```

*Files: 108*

---

## Frontend

### components

```
frontend/app/components/articles/Form.vue
frontend/app/components/articles/PatientOverview.vue
frontend/app/components/articles/Reader.vue
frontend/app/components/assignments/ContentPicker.vue
frontend/app/components/assignments/CreateDialog.vue
frontend/app/components/assignments/PatientList.vue
frontend/app/components/assignments/PickerItem.vue
frontend/app/components/auth/RoleSelector.vue
frontend/app/components/consents/AssistantContact.vue
frontend/app/components/content/RichTextEditor.vue
frontend/app/components/content/RichTextRenderer.vue
frontend/app/components/content/TagSelector.vue
frontend/app/components/invitations/LinkDialog.vue
frontend/app/components/layout/EmailVerificationBanner.vue
frontend/app/components/layout/Footer.vue
frontend/app/components/layout/Navbar.vue
frontend/app/components/layout/ThemeToggle.vue
frontend/app/components/notifications/Center.vue
frontend/app/components/patients/ContactStatus.vue
frontend/app/components/patients/Item.vue
frontend/app/components/patients/List.vue
frontend/app/components/patients/ProAccess.vue
frontend/app/components/programs/configurator/Editor.vue
frontend/app/components/programs/configurator/Item.vue
frontend/app/components/programs/configurator/Library.vue
frontend/app/components/programs/configurator/Stage.vue
frontend/app/components/programs/PatientAccess.vue
frontend/app/components/programs/PatientOverview.vue
frontend/app/components/programs/PatientProgress.vue
frontend/app/components/programs/viewer/Stage.vue
frontend/app/components/programs/VisibilityDialog.vue
frontend/app/components/questionnaires/Editor.vue
frontend/app/components/questionnaires/JsonImporter.vue
frontend/app/components/questionnaires/QuestionField.vue
frontend/app/components/questionnaires/QuestionItem.vue
frontend/app/components/ui/BottomSheet.vue
frontend/app/components/ui/ContentSkeleton.vue
frontend/app/components/ui/Modal.vue
frontend/app/components/ui/Pagination.vue
frontend/app/components/ui/ResponsiveDialog.vue
```
*Files: 40*

### pages

```
frontend/app/pages/content/articles/[id]/edit.vue
frontend/app/pages/content/articles/[id]/index.vue
frontend/app/pages/content/articles/index.vue
frontend/app/pages/content/articles/new.vue
frontend/app/pages/content/questionnaires/[id].vue
frontend/app/pages/content/questionnaires/index.vue
frontend/app/pages/content/questionnaires/new.vue
frontend/app/pages/dashboard.vue
frontend/app/pages/forgot-password.vue
frontend/app/pages/index.vue
frontend/app/pages/login.vue
frontend/app/pages/patients/[id]/index.vue
frontend/app/pages/patients/[id]/questionnaires/[submissionId].vue
frontend/app/pages/patients/index.vue
frontend/app/pages/programs/[id]/edit.vue
frontend/app/pages/programs/[id]/index.vue
frontend/app/pages/programs/index.vue
frontend/app/pages/programs/new.vue
frontend/app/pages/questionnaires/[id].vue
frontend/app/pages/questionnaires/index.vue
frontend/app/pages/reset-password.vue
frontend/app/pages/settings/security.vue
frontend/app/pages/verify-email.vue
```
*Files: 23*

### layouts

```
frontend/app/layouts/auth.vue
frontend/app/layouts/default.vue
```
*Files: 2*

### composables

```
frontend/app/composables/useBodyScrollLock.js
frontend/app/composables/useBreakpoint.js
frontend/app/composables/useClientReady.js
frontend/app/composables/useProgramPrice.js
frontend/app/composables/useReadingProgress.js
frontend/app/composables/useWebAuthn.js
```
*Files: 6*

### stores

```
frontend/app/stores/articles.js
frontend/app/stores/assignments.js
frontend/app/stores/auth.js
frontend/app/stores/notifications.js
frontend/app/stores/patients.js
frontend/app/stores/programs.js
frontend/app/stores/questionnaires.js
frontend/app/stores/ui.js
frontend/app/stores/user.js
```
*Files: 9*

### middleware

```
frontend/app/middleware/auth.global.js
frontend/app/middleware/program-manager.js
```
*Files: 2*

### plugins

```
frontend/app/plugins/api.js
```
*Files: 1*

---

## Deploy

```
deploy/backend.Dockerfile
deploy/docker-compose.yml
deploy/env/backend.env.example
deploy/env/compose.env.example
deploy/env/frontend.env.example
deploy/frontend.Dockerfile
deploy/nginx/default.conf
deploy/postgres/init/01-enable-pgcrypto.sql
deploy/scripts/backup.sh
deploy/scripts/deploy.sh
deploy/scripts/init-letsencrypt.sh
```

*Files: 11*

если тебе нужен какой-то файл, попроси прислать