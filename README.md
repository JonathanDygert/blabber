# blabber

Configure the url used to connect to mongo by setting `MONGO_URL_FILE` to a file containing only the desired url, without a trailing newline.
The docker stack is currently configured to use an external secret named mongo_url.