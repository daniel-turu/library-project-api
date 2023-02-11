from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
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


class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = User.objects.all()
    serializer_class = UserListSerializer

# # Category
# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated, IsStaffUser]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated, IsStaffUser]
#     serializer_class = CategorySerializer


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




