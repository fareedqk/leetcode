# LeetCode Solutions

This repository contains my solutions to various LeetCode problems, automatically synced from my LeetCode account.

## Sync Process

The solutions are synced using a GitHub Actions workflow, which runs weekly and can also be triggered manually.

## Repository Structure

```
.
└── my-folder
    ├── problems
    │   ├── problem_name
    │       ├── solution.py
    │   ├── problem_name
    │       ├── solution.py
    │   ...
```

Problem names organize solutions within the `my-folder` directory.

## File Naming Convention

Files are named according to the LeetCode problem number and the programming language used:

`problem<name>.<extension>`

## Languages

Solutions may be in various programming languages, namely Python depending on the problem requirements and personal preference.

## Syncing Details

The sync process uses GitHub Secrets to securely store LeetCode credentials:
- `LEETCODE_CSRF_TOKEN`
- `LEETCODE_SESSION`

These are used by the sync action to authenticate with LeetCode and fetch the latest solutions.

## Contributions

As this is an automated sync of personal solutions, direct contributions are not accepted. However, if you have suggestions or want to discuss a particular solution, feel free to open an issue.

## Disclaimer

These solutions are my personal attempts at solving LeetCode problems. They may not always represent the most optimal approach and are primarily for personal reference and learning purposes.
