from rest_framework import permissions

class IsCandidate( permissions.BasePermission ):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return getattr( request.user, 'role', None ) == 'candidate'

class IsEmployer( permissions.BasePermission ):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return getattr( request.user, 'role', None ) == 'employer'

class IsProfileOwner( permissions.BasePermission ):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsJobOwner( permissions.BasePermission ):
    def has_object_permission(self, request, view, obj):
        return obj.recruiter == request.user
