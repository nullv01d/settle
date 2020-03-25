from rest_framework import routers
from . import viewsets_api
from . import viewsets_auth


router = routers.DefaultRouter()
router.register(r'auth', viewsets_auth.AuthViewSet, basename='auth')
router.register(r'entity', viewsets_api.EntityViewSet)
router.register(r'entity-type', viewsets_api.EntityTypeViewSet)
router.register(r'entry-category', viewsets_api.EntryCategoryViewSet)
router.register(r'entry', viewsets_api.EntryViewSet)
router.register(r'settlement', viewsets_api.SettlementViewSet)
router.register(r'sale-summary', viewsets_api.SaleSummaryViewSet)
router.register(r'payment-mode', viewsets_api.PaymentModeViewSet)
