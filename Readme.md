# Scooper

[Scoop](https://scoop.sh/) is a fantastic package manager for windows (the reason I'm using one ;).

The instructions to install apps is fed through `.json` files stored in buckets... which for now I think is being added and maintained manually.

I happend to add instruction to install the new [mongo-shell (mongosh)](https://docs.mongodb.com/mongodb-shell/) as a [json file](https://github.com/joe733/scoop-extras/blob/mongosh/bucket/mongosh.json). But the prospect of checking for updates and editing this file manually is beyond me.

So I developed a python script which would scrape the download page for newer version of `mongosh`.

## Todo

- [ ] Setting up an action that would run this scrip periodically.
- [ ] Add a new commit to [`mongosh` branch](https://github.com/joe733/scoop-extras/tree/mongosh)
- [ ] Create a new PR if does not exists to add it to extras bucket.
