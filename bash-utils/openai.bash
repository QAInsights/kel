
# OpenAI API Key
# Get OpenAI API key from environment variable

openai_api_key() {
  if [ -z "$OPENAI_API_KEY" ]; then
    echo "OPENAI_API_KEY is not set"
    return 1
  fi
  echo "$OPENAI_API_KEY"
}


curl "https://api.openai.com/v1/assistants?order=desc&limit=20" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v1" | jq -r '.data[].id' | tee assistant_ids.txt

# Read assistant ids from file one by one
while read -r id; do
  echo "Deleting assistant $id"
  echo "curl https://api.openai.com/v1/assistants/$id"
  curl https://api.openai.com/v1/assistants/"$id" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v1" \
  -X DELETE
  sleep 1
done < assistant_ids.txt

# Delete assistant_ids.txt file
rm assistant_ids.txt

# Delete all files from OpenAI

curl https://api.openai.com/v1/assistants/asst_abc123/files/file-abc123 \
  -H 'Authorization: Bearer $OPENAI_API_KEY"' \
  -H 'Content-Type: application/json' \
  -H 'OpenAI-Beta: assistants=v1'





