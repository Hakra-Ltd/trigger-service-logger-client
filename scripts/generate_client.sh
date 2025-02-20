#!/bin/bash

# Exit on any error
set -e

usage() {
    echo "Usage: $0 -n <package_name> --i <API server IP> -b <branch name>"
    echo "Package name and IP required, branch name (optional) creates a branch before committing if passed"
    echo "Example: $0 -n listing_data_storage_client -i 0.0.0.0:8080"
    exit 1
}

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

while getopts "n:i:b:h" flag; do
    case $flag in
        n) name="$OPTARG";;
        i) ip="$OPTARG";;
        b) branch="$OPTARG";;
        h) echo "Usage: $0 -n <name> -a <age>"
           exit 0;;
        ?) echo "Invalid option. Usage: $0 -n <name> -a <age>"
           exit 1;;
    esac
done

if [ -z "$name" ]; then
    echo "Error: -n (package name) parameter is required"
    usage
fi

if [ -z "$ip" ]; then
    echo "Error: -i (API IP) parameter is required"
    usage
fi

echo "Package name: $name"
echo "API IP: $name"
echo "Branch name: $branch"

mkdir -p "${SCRIPT_DIR}/temp/client"

pushd "${SCRIPT_DIR}/temp/client" || exit

# download api client generator if not present
if ! test -f "${SCRIPT_DIR}/temp/openapi-generator-cli.jar"; then
  wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.9.0/openapi-generator-cli-7.9.0.jar -O "${SCRIPT_DIR}/temp/openapi-generator-cli.jar"
fi

# Generate the client
java -jar "${SCRIPT_DIR}/temp/openapi-generator-cli.jar" generate -g python -i "http://${ip}/openapi.json" "--additional-properties=library=asyncio,packageName=${name},tooling-extension=decimal"

popd || exit

# Move the generated client to the correct location
rm -rf "${SCRIPT_DIR}/../${name}/"
mv "${SCRIPT_DIR}/temp/client/${name}" "${SCRIPT_DIR}/.."

# Remove the temp directory
rm -rf "${SCRIPT_DIR}/temp/client"

if [ -n "$branch" ]; then
    git checkout -b "$branch"
    git branch -u origin/"$branch"
fi

# set upstream
git add "${SCRIPT_DIR}/../${name}"

git commit -m "Auto-update client"