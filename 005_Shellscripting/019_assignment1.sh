#!/bin/bash
# Author: Abhirami Kannan
# Purpose: Clone a Git repository, build the project using Maven, and deploy the WAR file to Tomcat.

#Write a shell script to clone a git repo and deploy maven based java application on tomcat.
#1. Download tomcat
#unzip
#webapps
#bin
#2. write shell script
#input: git repo.
#clone the repo.
#get inside
#mvn clean package
#target folder - war file
#copy *.war to webapps of tomcat
#$tomcat/bin/catalina.bat start

#usage: ./assignment1.sh

#!/bin/bash
# Author: Abhirami Kannan
# Purpose: Clone a Git repository, build the project using Maven, and deploy the WAR file to Tomcat.



# Check if the repository URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <repository-url>"
    exit 1
fi

# Assign the repository URL to a variable
repo_url=$1

# Clone the repository
git clone "$repo_url"
if [ $? -ne 0 ]; then
    echo "Failed to clone the repository."
    exit 1
fi

# Extract the repository name from the URL
repo_name=$(basename "$repo_url" .git)

# Change to the repository directory
cd "$repo_name" || exit

# Build the project using Maven
mvn clean package
if [ $? -ne 0 ]; then
    echo "Maven build failed."
    exit 1
fi

# Find the WAR file in the target directory
war_file=$(find target -name "*.war" | head -n 1)
if [ -z "$war_file" ]; then
    echo "WAR file not found."
    exit 1
fi

# Define the Tomcat webapps directory
tomcat_webapps="/path/to/tomcat/webapps"  # Replace with the actual path to your Tomcat webapps directory

# Copy the WAR file to the Tomcat webapps directory
cp "$war_file" "$tomcat_webapps"
if [ $? -ne 0 ]; then
    echo "Failed to copy the WAR file to the Tomcat webapps directory."
    exit 1
fi

# Start the Tomcat server
/path/to/tomcat/bin/catalina.sh start  # Replace with the actual path to your Tomcat catalina.sh script
if [ $? -ne 0 ]; then
    echo "Failed to start the Tomcat server."
    exit 1
fi

echo "Deployment successful."