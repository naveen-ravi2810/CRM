from functools import wraps

import jwt
from datetime import timedelta, datetime

from django.http import JsonResponse
from pytz import timezone
from root_admin.models import Admin
import bcrypt


def create_access_token(admin: Admin):
    ist = timezone("Asia/Kolkata")
    iat = datetime.now(ist)
    return jwt.encode(
        payload={
            "id": str(admin.id),
            "email": admin.email,
            "iat": iat,
            "exp": iat + timedelta(days=1),
            "is_admin": True,
        },
        key="1234568987654",
        algorithm="HS256",
    )


def decode_access_token(token: str):
    return jwt.decode(jwt=token, algorithms="HS256", key="1234568987654")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get("HTTP_AUTHORIZATION", None)
        if auth_header is None:
            return JsonResponse({"error": "Authorization header missing"}, status=401)
        try:
            scheme: str = auth_header.split()[0]
            token: str = auth_header.split()[1]
            if scheme.lower() is "bearer".lower():
                return JsonResponse({"error": "Invalid token scheme"}, status=403)
            payload = decode_access_token(token)
            if not payload.get("is_admin", False):
                return JsonResponse({"error": "Admin privileges required"}, status=403)
            request.jwt_payload = payload
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)
        return view_func(request, *args, **kwargs)

    return _wrapped_view
