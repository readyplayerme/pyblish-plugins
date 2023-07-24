# Welcome to the Ready Player Me Pyblish plugins contributing guide <!-- omit in toc -->

In this guide you will get an overview of the contribution workflow from opening an issue, creating a pull request, reviewing, and merging the pull request.

## New contributor guide

To get an overview of the project, read the [README](README.md).
Here are some resources to help you get started with open source contributions:

- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)
- Learn about [pre-commit hooks](https://pre-commit.com/)
- We use [black](https://black.readthedocs.io/en/stable/) formatting, but with a line-length of 120 characters.

## Getting started

To get familiar with pyblish, see [Pyblish by Example](https://learn.pyblish.com/).  
You should also be familiar with [Pydantic](https://docs.pydantic.dev/).

## Issues

#### Create a new issue

If you spot a problem with the plugins, [search if an issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments).
If a related issue doesn't exist, you can open a new issue using a relevant [issue form](https://github.com/readyplayerme/pyblish-plugins/issues/new/choose).

#### Solve an issue

Scan through our [existing issues](https://github.com/readyplayerme/pyblish-plugins/issues) to find one that interests you.
You can narrow down the search using `labels` as filters.

### Labels

Labels can help you find an issue you'd like to help with.
The [`good first issue` label](https://github.com/readyplayerme/pyblish-plugins/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) is for problems or updates we think are ideal for new joiners.

## Contribute

### Make changes locally

1. If you are a contributor from outside the Ready Player Me team, [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the (forked) repository to your local machine.

3. In your IDE, it's best to use a Python environment that fits Blender's Python version.
From the [Blender LTS versions](https://www.blender.org/download/lts/) that are currently maintained, choose the older one to determine the Python version.
We encourage using an environment manager such as [conda](https://docs.conda.io/en/latest/) or [pyenv](https://github.com/pyenv/pyenv).

4. Install or update the developer dependencies into your Python environment by navigating to the repository in a terminal and executing `pip install -e .[dev]`.

5. Run `pre-commit install` to set up the git hook scripts.

6. Install the plugins into Blender's user script folder as an editable package. <!-- TODO Explain how to do it -->

7. Create a working branch and prefix its name with _fix/_ if it's a bug fix, or _feature/_ if it's a new feature.
Start with your changes!

8. Write or update tests for your changes. <!-- TODO Explain how we do tests -->

9. Run tests and code linting & formatting locally.

### Commit your update

Once you are happy with your changes, it's time to commit them.
Use [Conventional Commit messages](https://www.conventionalcommits.org/en/v1.0.0/).  
[Sign](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) your commits!

Keep your individual commits small, so any breaking change can more easily be traced back to a commit.
A commit ideally only changes one single responsibility at a time.
If you keep the whole of your changes small and the branch short-lived, there's less risk to run into any other conflicts that can arise with the base.

Don't forget to [self-review](#self-review) to speed up the review process :zap:.

### Pull Request

When you're finished with the changes, create a __draft__ pull request, also known as a PR.

- Fill the "Ready for review" template so that we can review your PR. This template helps reviewers understand your changes as well as the purpose of your pull request.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
- If you are a contributor from outside the Ready Player Me team, enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge.
Once you submit your PR, a Ready Player Me team member will review your proposal.
We may ask questions or request additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments.
You can apply suggested changes directly through the UI.
You can make any other changes in your branch, and then commit them.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://github.com/skills/resolve-merge-conflicts) to help you resolve merge conflicts and other issues.

### Self review

You should always review your own PR first.

Make sure that you:

- [ ] Confirm that the changes meet the user experience and goals outlined in the design plan (if there is one).
- [ ] Update the version of the plugin.
- [ ] Update the documentation if necessary.
- [ ] If there are any failing checks in your PR, troubleshoot them until they're all passing.

### Merging your PR

Once your PR has the required approvals, a Ready Player Me team member will merge it.

We use a [squash & merge](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges#squash-and-merge-your-commits) by default to merge a PR.

The branch will be deleted automatically after the merge to prevent any more work being done the branch after it was merged.
