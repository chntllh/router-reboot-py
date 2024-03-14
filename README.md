# Personal script

Selenium using python to reboot my home routers

Accepts arguments 1, 2 and 3, together or seperately to restart the specific router.

Example
```
# Reboot all routers
python ./router.py 1 2 3

# Reboot only router 1
python ./router.py 1 

# Reboot router 1 and 3
python ./router.py 1 3
``` 

```
Network structure:

router1 (ISP router)
   |
   V
router2 (Main router)
   |
   V
router3 (Upstairs router)
```

Requires a `config.json` file in the same directory.

```json
{
    "1": {
        "website": "http://<router-1-website>",
        "username": "<username>",
        "password": "<password>"
    },
    "2": {
        "website": "http://<router-2-website>"
    },
    "3": {
        "website": "http://<router-3-website>",
        "password": "<password>"
    }
}
```