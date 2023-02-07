from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView



class LoginAPI(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user_serializer.data
                
            })
        else:
            return Response({"error": "Invalid credentials"})




class LibraryMemberCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LibraryMemberSerializer

class LibraryStaffMemberCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LibraryStaffMemberSerializer

class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer


# Category
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    serializer_class = CategorySerializer


# Book
class BookListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Search

class BookSearchView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search) |
                Q(ISBN__icontains=search) |
                Q(id__icontains=search)
            )

        return queryset
        


class IssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ReturnListCreateAPIView(generics.ListCreateAPIView):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

class RenewalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Renewal.objects.all()
    serializer_class = RenewalSerializer


# retrieve-update-delete

class IssueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ReturnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer

class RenewalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Renewal.objects.all()
    serializer_class = RenewalSerializer




# class MemberCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = MemberSerializer
#     authentication_classes = [SessionAuthentication,]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         response = {
#             'message': 'Member created successfully',
#             'data': serializer.data
#         }
#         return Response(response, status=status.HTTP_201_CREATED, headers=headers)


# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer







# class PostUserWritePermission(BasePermission):
#     message = 'Editing posts is restricted to the author only.'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True

#         return obj.author == request.user


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer





# class UserSignUpView(generics.CreateAPIView):
#     serializer_class = SignupUserSerializer
#     permission_classes = [AllowAny]

#     def perform_create(self, serializer):
#         user = serializer.save()
#         access_token = jwt.encode({'id': user.id}, 'secret', algorithm='HS256').decode('utf-8')
#         self.headers['Authorization'] = 'Bearer ' + access_token
#         return Response({'access_token': access_token})



#     def perform_create(self, serializer):
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         serializer.data['refresh'] = str(refresh)
#         serializer.data['access'] = str(refresh.access_token)


# class StaffSignUpView(generics.CreateAPIView):
#     serializer_class = SignupStaffSerializer

#     def perform_create(self, serializer):
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         serializer.data['refresh'] = str(refresh)
#         serializer.data['access'] = str(refresh.access_token)







# class LoginView(APIView):

#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     # permission_classes = [AllowAny]
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         access_token = jwt.encode({'id': user.id, 'is_staff': user.is_staff}, 'secret', algorithm='HS256').decode('utf-8')
#         return Response({
#             'access_token': access_token,
#             'permissions': ['create', 'update', 'delete'] if user.is_staff else []
#         })