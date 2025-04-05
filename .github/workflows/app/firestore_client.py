from google.cloud import firestore
from google.oauth2 import service_account

# 🔐 Full service account credentials (FOR DEV ONLY — DO NOT COMMIT)
service_account_info = {
  "type": "service_account",
  "project_id": "talentanalysis",
  "private_key_id": "18e96e993f36287b6a0814e8923ba63610db2615",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDbG1KCyK/WMr3l\\nF2QaL7ivAjZfDN2pfD2HNNMXnFkCvn8m3AAL1EiAdMbwI9d84sienHvdfkk2XNXG\\nWnaoDd1p867XPgm/8gtNg1BNqHXEEOOWrve83qiTm9FuZOMuwdZi6GPWGOl9XW6i\\nfNyrufnRUNJ82rfbP9cfMFKtW3b5V4mL4zH7XXDvkymJ0UCDns2OOoV1S0j6bzbp\\nhpV3GXDyh9MvCi0BvgWMk6e3ejOiIFjrJzIIN7r6+UXS8P/qj7ewI2KOns9GAam7\\niW/rOY9QYmGzSFdLsa9jJ1aMwATtRKDMPtqnz2mIJBCxFBvN9PrNWBU1jx9fxUR6\\nuQZkKDcnAgMBAAECggEAVGaA8SoXOb6QEZhiEghB7wA+K30MQcY++T8q9VRfoUP6\\nPODQD751My5Il6Zm0o+VUivbNuX3k75NBrxAKto0aSTaO8WFAfBd1Dz6CQAUZTNQ\\nR/IcMh/e9gU2tnycWp2GVNFJ6+Xqw0TjYioQ4wGfrragbkHeQtGjrzrxDiBGgyMz\\nhteMZaTpg9kO7wUsZk+xMplVmn2NF/iBvnA8naHYXd5bRFvXGtKIX8IZo11K7Z1o\\nAvPSi1DL8ByYr+IvQGGYuD6MhJRUTb2vcWBpa3D5i580USyAFKWMV1Qtc85fvKV6\\nQF98LI+DSaDPuBDPaX4Kb7ho8whhLqt7rP/YUJJYKQKBgQD4jm1KdqQiH6K5/dDj\\nvIfgC7B6pL1pvEqqJmW1YVoMz/8AuG3Jh7jXRXv/04BAeDqWKlkJtZe3u2ZrmAJf\\ndG/CnoaB62WX7WzxXjekYf6kQ+IzbChh/Z7oAK+24WXB2Q7ochqeqOW+xYYLALi8\\npW6YAcjLIqGwxAd1eY86i2Qa1QKBgQDhqx4yGcxKHAS6tVf5HvJtMAJrZU4u2fpO\\nkgHnw0JWRovvFUKEh0HmnGkpgNULkByQgLKueL19KOoAxRRB3SzlTT9AZOkynqmz\\nAnidjMFNQ8zQZvp3PDrIohgsGMq8fg40AiTWVeb2BcHgPaamnb72D0fFWVcyUmXQ\\nn0VDl9bQCwKBgQC1rW1nM0cPhi4sYsDv5VsvwXuSeZ3VjoLI0d4f8POgT9wli6j7\\n2I+cEjbrrI2fEgJIxtVkCm7GJl1bobWCThpul+7bQdN1dF7gIizro5E8Qj4xtgni\\nbj5beDz3oNL/GQgTkWuxsuSTR8+NdU6S3Rz0UMGS8VJcYTzOejbd5QsbrQKBgFIM\\neUoV/yTi0wVfccDt846nafnKN4bpUgzHIVI2uCPOOoqO3ER7OQazz7h7UvqFRx1y\\n7YRp+dtLyOjGvvrDg9NLJrgu+GqjLWgceeYuiwmgoRMUnfREPcs8xDUkPnISEu/t\\n557WVMcWiMsTH0htCkVEgP/L39w4ATS8894DkuLJAoGAFtQpYx6T2wlImIO2UAyW\\nojyG4JJTaOzQwDqrt7lME2GIIU87LZLID+4ewpEIHRs2PbAZ8lsBljK9ekdNVxlq\\n2UPwMi7IFSVFjgXALUq79D2xGTUhjJPOrKzU6HOAtKG/rpxZKmKv1xs1iBXdYtGU\\nqNwW2wcuZ0+O0Z10yZLDqJM=\\n-----END PRIVATE KEY-----\\n",
  "client_email": "firebase-adminsdk-fbsvc@talentanalysis.iam.gserviceaccount.com",
  "client_id": "117368731954312849944",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc@talentanalysis.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# 🔐 Create credentials from dict
credentials = service_account.Credentials.from_service_account_info(service_account_info)

# 🔥 Initialize Firestore
db = firestore.Client(credentials=credentials, project="talentanalysis")

# ✅ Save data
def save_candidate_data(candidate_id, data):
    doc_ref = db.collection("candidates").document(candidate_id)
    doc_ref.set(data)

def get_candidate_data(candidate_id):
    doc_ref = db.collection("candidates").document(candidate_id)
    return doc_ref.get().to_dict()
