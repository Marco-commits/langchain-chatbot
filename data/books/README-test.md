MVF servicer Apollo
Usage
To install the package
Run npm install @mvf/servicer-apollo

Configuration
Set the following environment variables in your project

ENVIRONMENT_FILE should be set to development | testing | staging | production
APOLLO_SERVER_PORT=8080


setupApplication();
Contributing
Setup
Run make to build the container
Run make shell to enter the container
Run npm install to install dependencies
Refer to package.json for commands

After merging
After you have merged a PR to master, you need to rebuild and publish your changes.

Checkout master git checkout master && git pull
Use one of the following make publish commands to publish changes: - make publish kind=patch - Use this if your change is a bug fix and is backwards compatible. - make publish kind=minor - Use this if your change adds new functionality and is backwards compatible. - make publish kind=major - Use this if your change is not backwards compatible.