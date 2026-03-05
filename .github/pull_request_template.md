# Summary
This pull request introduces a standardized pull request template and a self-review checklist to improve the quality and clarity of contributions in the repository. The goal is to ensure that every pull request contains a clear explanation of the changes made, the reason for the change, and how the changes were tested.

By adding a template, contributors are guided to describe their work properly instead of submitting pull requests with minimal or unclear descriptions. This helps reviewers understand the purpose of the change quickly and improves collaboration within the project.

# Changes
- Added a pull request template in `.github/pull_request_template.md` to guide contributors when creating pull requests.
- The template includes sections such as **Summary**, **Changes**, and **Checklist** to ensure consistent documentation.
- Added a **self-review checklist** to help contributors verify their work before submitting a pull request.
- Added a documentation file `docs/pr-checklist.md` that explains the self-review process and best practices when submitting a pull request.
- Improved repository documentation to make the contribution workflow clearer and easier to follow.

# How to test
1. Create a new branch and make a small change in the repository.
2. Open a new Pull Request on GitHub.
3. Verify that the pull request template appears automatically.
4. Fill in the **Summary**, **Changes**, and **Checklist** sections to describe the update.
5. Confirm that the checklist helps ensure the pull request is properly documented.

# Checklist
- [ ] I ran `pytest -q` locally and all tests passed
- [ ] I updated documentation where necessary
- [ ] I kept the pull request focused on one logical change
- [ ] I checked formatting and naming consistency
- [ ] I confirmed that no secrets or large unnecessary files were added
