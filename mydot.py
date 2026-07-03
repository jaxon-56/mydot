#Written by: https://mydot.one/profile/abas3695
import os
import mimetypes
import requests


class MyDotAPI:

    def __init__(self):
        self.session = requests.Session()

        self.headers = {
            "accept": "application/json, text/plain, */*",
            "origin": "https://mydot.one",
            "referer": "https://mydot.one/",
            "user-agent": "Mozilla/5.0",
        }

    def login(self, username, password):
        url = "https://api.mydot.one/mydot/api/v1/auth/login/"

        payload = {
            "identifier": username,
            "password": password
        }

        r = self.session.post(
            url,
            headers={
                **self.headers,
                "content-type": "application/json"
            },
            json=payload
        )

        try:
            return r.json()
        except:
            return r.text

    def profile(self):
        url = "https://api.mydot.one/mydot/api/v1/auth/profile/"

        r = self.session.get(
            url,
            headers=self.headers
        )

        try:
            return r.json()
        except:
            return r.text

    def get_user_profile(self, username):
        url = f"https://api.mydot.one/mydot/api/v1/auth/profile/{username}"

        r = self.session.get(
            url,
            headers=self.headers
        )

        try:
            return r.json()
        except:
            return r.text

    def update_profile(
        self,
        display_name=None,
        bio=None,
        location=None,
        website=None,
        birthdate=None,
        gender=None,
        profile_visibility=None
    ):
        url = "https://api.mydot.one/mydot/api/v1/auth/profile/"

        data = {}

        if display_name is not None:
            data["display_name"] = display_name

        if bio is not None:
            data["bio"] = bio

        if location is not None:
            data["location"] = location

        if website is not None:
            data["website"] = website

        if birthdate is not None:
            data["birthdate"] = birthdate

        if gender is not None:
            data["gender"] = gender

        if profile_visibility is not None:
            data["profile_visibility"] = profile_visibility

        r = self.session.patch(
            url,
            headers={
                **self.headers,
                "content-type": "application/json"
            },
            json=data
        )

        try:
            return r.json()
        except:
            return r.text

    def notifications(self, page_size=50):
        url = "https://api.mydot.one/mydot/api/v1/notifications/"

        r = self.session.get(
            url,
            headers=self.headers,
            params={
                "page_size": page_size
            }
        )

        try:
            return r.json()
        except:
            return r.text

    def conversations(self, tab="all"):
        url = "https://api.mydot.one/chat/api/conversations/summaries"

        r = self.session.get(
            url,
            headers=self.headers,
            params={
                "tab": tab
            }
        )

        try:
            return r.json()
        except:
            return r.text

    def trending_hashtags(self):
        url = "https://api.mydot.one/mydot/api/v1/dots/hashtags/trending/"

        r = self.session.get(
            url,
            headers=self.headers
        )

        try:
            return r.json()
        except:
            return r.text
    def timeline(self, page_size=40):
        url = "https://api.mydot.one/mydot/api/v1/feed/suggestions/timeline/"

        r = self.session.get(
            url,
            headers=self.headers,
            params={
                "page_size": page_size
            }
        )

        try:
            return r.json()
        except:
            return r.text

    def followers(self, username, page_size=20, cursor=None):
        url = f"https://api.mydot.one/mydot/api/v1/auth/{username}/followers/"

        params = {
            "page_size": page_size
        }

        if cursor:
            params["cursor"] = cursor

        r = self.session.get(
            url,
            headers=self.headers,
            params=params
        )

        try:
            return r.json()
        except:
            return r.text

    def following(self, username, page_size=20, cursor=None):
        url = f"https://api.mydot.one/mydot/api/v1/auth/{username}/following/"

        params = {
            "page_size": page_size
        }

        if cursor:
            params["cursor"] = cursor

        r = self.session.get(
            url,
            headers=self.headers,
            params=params
        )

        try:
            return r.json()
        except:
            return r.text

    def user_activity(self, user_id, action_type="like", page_size=None, cursor=None):
        url = f"https://api.mydot.one/mydot/api/v1/dots/user/{user_id}/activity/"

        params = {
            "action_type": action_type
        }

        if page_size is not None:
            params["page_size"] = page_size

        if cursor:
            params["cursor"] = cursor

        r = self.session.get(
            url,
            headers=self.headers,
            params=params
        )

        try:
            return r.json()
        except:
            return r.text

    def create_avatar_upload(self, filename, content_type=None):
        if content_type is None:
            content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"

        url = "https://api.mydot.one/mydot/api/v1/auth/profile/avatar/upload/"

        r = self.session.post(
            url,
            headers={
                **self.headers,
                "content-type": "application/json"
            },
            json={
                "filename": os.path.basename(filename),
                "content_type": content_type
            }
        )

        try:
            return r.json()
        except:
            return r.text

    def create_header_upload(self, filename, content_type=None):
        if content_type is None:
            content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"

        url = "https://api.mydot.one/mydot/api/v1/auth/profile/header/upload/"

        r = self.session.post(
            url,
            headers={
                **self.headers,
                "content-type": "application/json"
            },
            json={
                "filename": os.path.basename(filename),
                "content_type": content_type
            }
        )

        try:
            return r.json()
        except:
            return r.text
    def upload_file(self, upload_url, file_path, content_type=None):
        if content_type is None:
            content_type = (
                mimetypes.guess_type(file_path)[0]
                or "application/octet-stream"
            )

        with open(file_path, "rb") as f:
            r = requests.put(
                upload_url,
                data=f,
                headers={
                    "Content-Type": content_type
                }
            )

        return r.status_code in (200, 201, 204)

    def confirm_avatar_upload(self, key):
        url = "https://api.mydot.one/mydot/api/v1/auth/profile/avatar/upload/confirm/"

        r = self.session.post(
            url,
            headers={
                **self.headers,
                "content-type": "application/json"
            },
            json={
                "key": key
            }
        )

        try:
            return r.json()
        except:
            return r.text

    def confirm_header_upload(self, key):
        url = "https://api.mydot.one/mydot/api/v1/auth/profile/header/upload/confirm/"

        r = self.session.post(
            url,
            headers={
                **self.headers,
                "content-type": "application/json"
            },
            json={
                "key": key
            }
        )

        try:
            return r.json()
        except:
            return r.text

    def set_avatar(self, file_path):
        info = self.create_avatar_upload(file_path)

        if not isinstance(info, dict):
            return info

        if "upload_url" not in info:
            return info

        ok = self.upload_file(
            info["upload_url"],
            file_path
        )

        if not ok:
            return {
                "success": False,
                "message": "Upload failed"
            }

        return self.confirm_avatar_upload(
            info["key"]
        )

    def set_header(self, file_path):
        info = self.create_header_upload(file_path)

        if not isinstance(info, dict):
            return info

        if "upload_url" not in info:
            return info

        ok = self.upload_file(
            info["upload_url"],
            file_path
        )

        if not ok:
            return {
                "success": False,
                "message": "Upload failed"
            }

        return self.confirm_header_upload(
            info["key"]
        )
