from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import  Empleado, Tecnico, Productora, Creacion


# ====================
# EMPLEADO
# ====================

def empleado(request):
    empleados = Empleado.objects.all()
    return render(request, "empleado.html", {'empleados': empleados})

def nuevoEmpleado(request):
    return render(request, "nuevoEmpleado.html")

def guardarEmpleado(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    fecha_ingreso = request.POST["fecha_ingreso"]
    Empleado.objects.create(nombre=nombre, apellido=apellido, fecha_ingreso=fecha_ingreso)
    messages.success(request, "Empleado guardado exitosamente")
    return redirect('/empleado')

def editarEmpleado(request, id):
    empleadoEditar = Empleado.objects.get(id=id)
    return render(request, "editarEmpleado.html", {'empleadoEditar': empleadoEditar})

def procesarEdicionEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.nombre = request.POST["nombre"]
    empleado.apellido = request.POST["apellido"]
    empleado.fecha_ingreso = request.POST["fecha_ingreso"]
    empleado.save()
    messages.success(request, "Empleado actualizado exitosamente")
    return redirect('/empleado')

def eliminarEmpleado(request, id):
    Empleado.objects.get(id=id).delete()
    return redirect('/empleado')


# ====================
# TECNICO
# ====================

def tecnico(request):
    tecnicos = Tecnico.objects.all()
    return render(request, "tecnico.html", {'tecnicos': tecnicos})

def nuevoTecnico(request):
    empleados = Empleado.objects.all()  # mostrar empleados existentes
    return render(request, "nuevoTecnico.html", {'empleados': empleados})

def guardarTecnico(request):
    id_empleado = request.POST["empleado_id"]
    especialidad = request.POST["especialidad"]
    empleado = Empleado.objects.get(id=id_empleado)
    Tecnico.objects.create(empleado=empleado, especialidad=especialidad)
    messages.success(request, "Técnico guardado exitosamente")
    return redirect('/tecnico')

def editarTecnico(request, id):
    tecnicoEditar = Tecnico.objects.get(empleado_id=id)
    return render(request, "editarTecnico.html", {'tecnicoEditar': tecnicoEditar})

def procesarEdicionTecnico(request, id):
    tecnico = Tecnico.objects.get(empleado_id=id)
    tecnico.especialidad = request.POST["especialidad"]
    tecnico.save()
    messages.success(request, "Técnico actualizado exitosamente")
    return redirect('/tecnico')

def eliminarTecnico(request, id):
    Tecnico.objects.get(empleado_id=id).delete()
    return redirect('/tecnico')


# ====================
# PRODUCTORA
# ====================

def productora(request):
    productoras = Productora.objects.all()
    return render(request, "productora.html", {'productoras': productoras})

def nuevaProductora(request):
    return render(request, "nuevaProductora.html")

def guardarProductora(request):
    nombre = request.POST["nombre"]
    pais = request.POST["pais"]
    Productora.objects.create(nombre=nombre, pais=pais)
    messages.success(request, "Productora guardada exitosamente")
    return redirect('/productora')

def editarProductora(request, id):
    productoraEditar = Productora.objects.get(id=id)
    return render(request, "editarProductora.html", {'productoraEditar': productoraEditar})

def procesarEdicionProductora(request, id):
    productora = Productora.objects.get(id=id)
    productora.nombre = request.POST["nombre"]
    productora.pais = request.POST["pais"]
    productora.save()
    messages.success(request, "Productora actualizada exitosamente")
    return redirect('/productora')

def eliminarProductora(request, id):
    Productora.objects.get(id=id).delete()
    return redirect('/productora')


# ====================
# CREACION
# ====================

def creacion(request):
    creaciones = Creacion.objects.all()
    return render(request, "creacion.html", {'creaciones': creaciones})

def nuevaCreacion(request):
    tecnicos = Tecnico.objects.all()
    productoras = Productora.objects.all()
    return render(request, "nuevaCreacion.html", {'tecnicos': tecnicos, 'productoras': productoras})

def guardarCreacion(request):
    descripcion = request.POST["descripcion"]
    fecha_creacion = request.POST["fecha_creacion"]
    tecnico_id = request.POST["tecnico_id"]
    productora_id = request.POST["productora_id"]
    tecnico = Tecnico.objects.get(empleado_id=tecnico_id)
    productora = Productora.objects.get(id=productora_id)
    Creacion.objects.create(descripcion=descripcion, fecha_creacion=fecha_creacion, tecnico=tecnico, productora=productora)
    messages.success(request, "Creación guardada exitosamente")
    return redirect('/creacion')

def editarCreacion(request, id):
    creacionEditar = Creacion.objects.get(id=id)
    tecnicos = Tecnico.objects.all()
    productoras = Productora.objects.all()
    return render(request, "editarCreacion.html", {'creacionEditar': creacionEditar, 'tecnicos': tecnicos, 'productoras': productoras})

def procesarEdicionCreacion(request, id):
    creacion = Creacion.objects.get(id=id)
    creacion.descripcion = request.POST["descripcion"]
    creacion.fecha_creacion = request.POST["fecha_creacion"]
    creacion.tecnico = Tecnico.objects.get(empleado_id=request.POST["tecnico_id"])
    creacion.productora = Productora.objects.get(id=request.POST["productora_id"])
    creacion.save()
    messages.success(request, "Creación actualizada exitosamente")
    return redirect('/creacion')

def eliminarCreacion(request, id):
    Creacion.objects.get(id=id).delete()
    return redirect('/creacion')
