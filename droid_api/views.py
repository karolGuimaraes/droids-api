from droid_api.models import *
from rest_framework.decorators import api_view
from droid_api.serializers import DemandaSerializer, ContaSerializer
from django.http import JsonResponse


@api_view(['GET'])
def listar_demandas(request, format=None):
    try:
        demandas = Demanda.objects.all().order_by('id')
        serializer = DemandaSerializer(demandas, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except:
        return JsonResponse({'Error':'Internal server error :('}, status=500)


@api_view(['POST'])
def adicionar_demanda(request):
    try:
        serializer = DemandaSerializer(data=request.data)
        if serializer.is_valid():
            endereco = request.data.get('endereco_entrega', '')
            peca = request.data.get('peca', '')
            username = request.data.get('anunciante', '')
            conta = Conta.objects.filter(username=username)
            if conta:
                conta = conta[0]
                if Endereco.objects.filter(**endereco):
                    endereco_entrega = Endereco.objects.filter(**endereco).last()
                else:
                    endereco_entrega = Endereco.objects.create(**endereco)

                peca = Peca.objects.create(**peca)
                demanda = Demanda.objects.create(peca=peca, anunciante=conta, endereco_entrega=endereco_entrega)
                serializer = DemandaSerializer(demanda)
            
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse({'Error':'Anunciante {} não foi encontrado '.format(username)}, status=400)
        return JsonResponse(serializer.errors, status=400)
    except:
        return JsonResponse({'Error':'Internal server error :('}, status=500)


@api_view(['PUT'])
def editar_demanda(request):
    try:
        serializer = DemandaSerializer(data=request.data)
        if serializer.is_valid():
            id = request.data.get('demanda', '')
            demanda = Demanda.objects.filter(id=id)
            if demanda:
                demanda = demanda[0]
                peca = request.data.get('peca', '')
                Peca.objects.filter(id=demanda.peca.id).update(**peca)
                endereco = request.data.get('endereco_entrega', '')
                Endereco.objects.filter(id=demanda.endereco_entrega.id).update(**endereco)

                serializer = DemandaSerializer(demanda)
                return JsonResponse(serializer.data, status=200)
            else:
                return JsonResponse({'Error':'Demanda não foi encontrada pelo número {}'.format(id)}, status=404)
        return JsonResponse(serializer.errors, status=400)
    except:
        return JsonResponse({'Error':'Internal server error :('}, status=500)


@api_view(['DELETE'])
def excluir_demanda(request, format=None):
    try:
        id = request.data.get('demanda', '')
        try:
            demanda = Demanda.objects.get(id=id)
            demanda.delete()
            return JsonResponse({'success':'Demanda excluída com sucesso!'}, status=200)
        except:
            return JsonResponse({'Error':'Demanda não foi encontrada pelo número {}'.format(id)}, status=404)
    except:
        return JsonResponse({'Error':'Internal server error :('}, status=500)


@api_view(['PUT'])
def finalizar_demanda(request):
    try:
        id = request.data.get('demanda', '')
        demanda = Demanda.objects.filter(id=id)
        if demanda:
            demanda = demanda[0]
            if not demanda.finalizada:
                demanda.finalizada = True
                demanda.save()
                return JsonResponse({'success':'Demanda finalizada com sucesso!'}, status=200)
            else:
                serializer = DemandaSerializer(demanda)
                return JsonResponse({'success':'A demanda já foi finalizada anteriormente!'}, status=200)
        else:
            return JsonResponse({'Error':'Demanda não foi encontrada pelo número {}'.format(id)}, status=404)
    except:
        return JsonResponse({'Error':'Internal server error :('}, status=500)


@api_view(['POST'])
def criar_usuario(request, format=None):
    admin = request.data.get('admin', 'Nao')
    try:
        serializer = ContaSerializer(data=request.data)
        if serializer.is_valid():
            conta = serializer.save()
            conta.is_active = True
            if admin.upper() == "SIM":
                conta.is_staff = True
                conta.is_superuser = True
            conta.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    except:
        return JsonResponse({'Error':'Internal server error :('}, status=500)