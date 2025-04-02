#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <file_name> <difficulty> <source> <comma_separated_destinations>"
  exit 1
fi

# Assign arguments to variables
file_name=$1
difficulty=$2
source=$3
destinations=$4

# Define the source path
source_path="leetcode/$source/$difficulty/$file_name"

# Loop through each destination
IFS=',' read -ra dest_array <<< "$destinations"
for destination in "${dest_array[@]}"; do
  # Define the destination path
  dest_dir="leetcode/$destination/$difficulty"
  dest_path="$dest_dir/$file_name"

  # Create the destination directory if it doesn't exist
  mkdir -p "$dest_dir"

  # Create the symbolic link with a relative path
  ln -sf "../../$source/$difficulty/$file_name" "$dest_path"
done

echo "Links created successfully."