
# Git 常用命令速查表


| Command         | 用法说明                                                                 | 使用示例                                                                                  |
| :-------------- | :----------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| `clone`         | 将远程仓库克隆到本地的新目录中                                           | `git clone https://github.com/user/repo.git`                                              |
| `init`          | 初始化一个新的空的 Git 仓库或重新初始化一个已存在的仓库                   | `git init` 在当前目录初始化新仓库                                                           |
| `add`           | 将文件内容添加到**暂存区**                                               | `git add .` 添加所有修改；`git add filename.txt` 添加特定文件                              |
| `mv`            | 移动或重命名文件、目录或符号链接                                           | `git mv oldfile.txt newfile.txt`                                                          |
| `restore`       | 恢复**工作区**的文件                                                     | `git restore filename.txt` 丢弃工作区对某个文件的修改                                      |
| `rm`            | 从**工作区**和**暂存区**中删除文件                                         | `git rm filename.txt`                                                                     |
| `status`        | 显示**工作区**和**暂存区**的状态                                         | `git status`                                                                              |
| `commit`        | 将**暂存区**的更改提交到本地仓库                                         | `git commit -m "提交说明"`                                                                 |
| `branch`        | 列出、创建或删除分支                                                     | `git branch` 查看分支；`git branch new-branch` 创建新分支；`git branch -d branch-name` 删除分支 |
| `checkout`      | 切换分支或恢复文件                                                       | `git checkout branch-name` 切换分支；`git checkout -- filename.txt` 撤销对文件的修改        |
| `switch`        | 切换分支 (Git 2.23+)                                                     | `git switch branch-name`                                                                  |
| `merge`         | 将指定分支的更改合并到当前分支                                             | `git merge branch-name`                                                                   |
| `rebase`        | 将当前分支的提交在另一个基点之上重新应用（**变基**）                       | `git rebase main`                                                                         |
| `log`           | 显示提交日志                                                             | `git log`；`git log --oneline` 简洁模式；`git log -p` 查看详细修改                         |
| `diff`          | 显示提交之间、提交与工作区之间的更改内容                                   | `git diff` 查看未暂存修改；`git diff --staged` 查看已暂存修改                              |
| `fetch`         | 从远程仓库下载对象和引用，但不自动合并                                   | `git fetch origin`                                                                        |
| `pull`          | 从远程仓库获取并集成更改（默认为 `fetch` + `merge`）                      | `git pull origin main`                                                                    |
| `push`          | 将本地提交推送到远程仓库                                                   | `git push origin main`                                                                    |
| `stash`         | 临时保存工作区的修改                                                     | `git stash` 保存当前修改；`git stash pop` 恢复最近暂存的修改                               |
| `reset`         | 将当前 `HEAD` 重置到指定状态                                              | `git reset HEAD~1` 回退到上一个提交（保留修改）；`git reset --hard HEAD~1` 强制回退并丢弃修改 |
| `revert`        | 创建一个新的提交来撤销指定提交的更改（安全操作）                           | `git revert commit-hash`                                                                  |
| `tag`           | 创建、列出、删除或验证标签对象                                             | `git tag v1.0.0` 创建标签；`git push origin v1.0.0` 推送标签到远程                         |





#  使用提示

*   **核心概念**：
    *   **工作区 (Workspace)**：你直接编辑文件的地方。
    *   **暂存区 (Index / Stage)**：通过 `git add` 将修改添加到这里，准备下次提交。
    *   **本地仓库 (Repository)**：通过 `git commit` 将暂存区的内容提交到这里，形成一次历史记录。
    *   **远程仓库 (Remote)**：如 GitHub 上的仓库，通过 `git push`/`git pull` 与之同步。

*   **谨慎操作**：`git reset --hard` 和 `git rebase` 等命令可能会重写历史，在操作重要分支（如 `main`）前务必确认理解其后果。对已推送的提交，通常更推荐使用 `git revert` 来撤销更改。

*   **查看帮助**：想了解某个命令的更多选项和细节，可以使用 `git help <command>` 命令查看其完整帮助文档。




要使用 Git 管理 GitHub 上的项目链接（如您提供的国家气象中心图片下载器），请按照以下步骤操作：

### 1. **克隆仓库到本地**
```bash
git clone https://github.com/wty20191019/NMC_downloader.git
cd NMC_downloader
```

### 2. **日常管理操作**
| 操作 | 命令 | 说明 |
|------|------|------|
| **查看状态** | `git status` | 查看文件修改状态 |
| **添加文件** | `git add <文件名>`或`git add .`(add all) | 将修改加入暂存区 |
| **提交变更** | `git commit -m "描述信息"` | 提交变更到本地仓库 |
| **推送更新** | `git push origin main` | 上传到 GitHub 仓库 |
| **拉取更新** | `git pull` | 获取远程最新代码 |

### 3. **管理项目链接**
对于项目中的链接（如气象数据源）：
```bash
# 查看文件历史（含链接变更）
git log -- nmc_downloader/nmc_radar_downloader.py

# 恢复特定版本的链接
git checkout <commit-id> -- path/to/file.py
```

### 4. **分支管理**
```bash
git branch feature/new-download-source  # 创建新分支
git checkout feature/new-download-source  # 切换分支
# 修改链接后提交...
git push -u origin feature/new-download-source
```

### 5. **通过 .gitignore 忽略不需要管理的文件**
创建 `.gitignore` 文件：
```
# 忽略下载的图片数据
nmc_radar_downloader/
nmc_weatherchartWithRadar_downloader/

# 忽略系统文件
.DS_Store
Thumbs.db
```

### 实际应用场景示例：
**修改数据源链接后提交：**
```bash
# 1. 修改源代码中的URL
vim nmc_downloader/nmc_radar_downloader.py

# 2. 提交变更
git add nmc_downloader/nmc_radar_downloader.py
git commit -m "更新雷达数据源URL"
git push
```

**恢复旧版链接配置：**
```bash
# 查找历史记录
git log --oneline -- nmc_downloader/nmc_radar_downloader.py

# 恢复特定版本 (例如 abc123)
git checkout abc123 -- nmc_downloader/nmc_radar_downloader.py
```

> **重要提示**：
> 1. 项目中的气象图片实际存储在 `nmc_*_downloader/` 目录，建议通过 `.gitignore` 忽略这些目录
> 2. 链接变更应通过提交代码修改实现，不要直接提交下载的图片数据
> 3. 定期使用 `git pull` 获取原作者的最新更新

这样既能有效管理项目代码和链接配置，又能避免仓库被大量图片数据膨胀。








