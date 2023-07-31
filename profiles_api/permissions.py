from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update own status"""

    #Overriding permission checking method
    def has_object_permission(self, request, view, obj):
        """Check user is trying to update own status"""
        #Return true if request is a non-Overriding request
        if request.method in permissions.SAFE_METHODS:
            return True
        #Returns true only when the user who made the request owns the status
        return obj.user_profile.id == request.user.id
