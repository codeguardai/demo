# Demo

Demo of [GuardAI](https://github.com/codeguardai/guardai)

This demo provides an overview of how the GuardAI tool can be used both in a CI pipeline and locally via the command line.

## CI Integration with GitHub Actions

GuardAI can be integrated into your CI pipeline using GitHub Actions/Workflows. In this example, the workflow is configured to run on pull requests targeting the `main` branch. The action scans the code in the specified directory and generates a report. The workflow then posts the results as a comment on the pull request.

- **Workflow File**: [Demo CI Workflow](https://github.com/codeguardai/demo/.github/workflows/ci.yml)
- **Pull Request Example**: [#123: Demonstration PR](https://github.com/codeguardai/demo/pull/1)

### Pull Request Workflow

1. **Run GuardAI Action**: The action scans the code in the `src` directory and outputs the results to a file (`guardai_output.txt`).
2. **Comment on PR**: The content of the `guardai_output.txt` file is automatically posted as a collapsible comment on the pull request, allowing reviewers to easily view the scan results.

Example of how the GuardAI output is commented on a PR:

![PR Comment Example]()  
_Placeholder GIF: This GIF represents how GuardAI comments its findings directly in a pull request. Replace with an actual GIF showing the feature in action._

## Local CLI Usage

GuardAI is also designed to be used locally via the command line, allowing developers to scan their code for vulnerabilities before pushing changes to a repository. This ensures that issues can be caught early in the development process.

### How to Use GuardAI Locally

1. **Run GuardAI from the command line**:

   ```bash
   pip install guardai
   export OPENAI_API_KEY=<KEY>
   guardai --provider openai --directory ./src
   ```

2. **Review the output**: GuardAI will scan the code in the specified directory and output the results directly in your terminal or to a specified output file.

Example of GuardAI CLI usage:

![CLI Demo](cli-demo.gif)

Summary:

For more information, check out the [GuardAI repository](https://github.com/codeguardai/guardai).
