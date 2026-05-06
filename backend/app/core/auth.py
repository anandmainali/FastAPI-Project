import httpx
from fastapi import Depends, HTTPException, Request, status
from clerk_backend_api.security import AuthenticationRequestOptions
from app.core.config import settings
from app.core.clerk import clerk

class AuthUser:
    def __init__(self, user_id: str, org_id: str, org_permissions: list):
        self.user_id = user_id
        self.ord_id = org_id
        self.org_permissions = org_permissions

    def has_permission(self, permission: str) -> bool:
        return permission in self.org_permissions
    
    @property
    def can_view(self) -> bool:
        return self.has_permission("org:tasks:view")
    
    @property
    def can_create(self) -> bool:
        return self.has_permission("org:tasks:create")
    
    @property
    def can_edit(self) -> bool:
        return self.has_permission("org:tasks:edit")
    
    @property
    def can_delete(self) -> bool:
        return self.has_permission("org:tasks:delete")