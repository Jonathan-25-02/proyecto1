from django.urls import path
from . import views

urlpatterns = [

    

    # Empleado
    path('', views.empleado),
    path('empleado', views.empleado),
    path('nuevoEmpleado', views.nuevoEmpleado),
    path('guardarEmpleado', views.guardarEmpleado),
    path('eliminarEmpleado/<id>', views.eliminarEmpleado),
    path('editarEmpleado/<id>', views.editarEmpleado),
    path('procesarEdicionEmpleado/<id>', views.procesarEdicionEmpleado),

    # Técnico
    path('tecnico', views.tecnico),
    path('nuevoTecnico', views.nuevoTecnico),
    path('guardarTecnico', views.guardarTecnico),
    path('eliminarTecnico/<id>', views.eliminarTecnico),
    path('editarTecnico/<id>', views.editarTecnico),
    path('procesarEdicionTecnico/<id>', views.procesarEdicionTecnico),

    # Productora
    path('productora', views.productora),
    path('nuevaProductora', views.nuevaProductora),
    path('guardarProductora', views.guardarProductora),
    path('eliminarProductora/<id>', views.eliminarProductora),
    path('editarProductora/<id>', views.editarProductora),
    path('procesarEdicionProductora/<id>', views.procesarEdicionProductora),

    # Creación
    path('creacion', views.creacion),
    path('nuevaCreacion', views.nuevaCreacion),
    path('guardarCreacion', views.guardarCreacion),
    path('eliminarCreacion/<id>', views.eliminarCreacion),
    path('editarCreacion/<id>', views.editarCreacion),
    path('procesarEdicionCreacion/<id>', views.procesarEdicionCreacion),
]
