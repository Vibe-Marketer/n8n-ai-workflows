# Plan for Repository Cleanup

This document outlines the plan to review and update all markdown files in the repository.

## 1. File Identification

- A script was used to generate a complete file tree, from which all markdown files were extracted. A total of 61 markdown files were found. This includes `README.md` files within workflow directories, and root-level documents like `README.md`, `CONTRIBUTING.md`, `roadmap.md`, and `changelog.md`.

## 2. Content Review and Modification

Each `README.md` file will be reviewed and edited to perform the following actions:

- **Remove Sales Copy**: All promotional text, especially the sections starting with "⚠️ WARNING: Stop Building Basic Automations For Peanuts. 🚫", will be removed.
- **Remove "Skool" References**: All links and mentions of the "Skool" community will be removed.
- **Remove External GitHub Repository Links**: Any links to GitHub repositories other than the current one will be removed. This primarily refers to links containing `oxbshw`.
- **Retain Essential Information**: The basic information required to understand and launch the project/workflow will be preserved.

## 3. File Deletion

- A separate file, `FILES_TO_DELETE.md`, lists files recommended for deletion.
- These files will be deleted only after receiving explicit user approval.

## 4. Execution and Confirmation

- The plan will be executed only after user confirmation.
- All changes will be reviewed before finalizing the task.