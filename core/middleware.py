from django_tenants.middleware.main import TenantMainMiddleware


class TenantMiddleware(TenantMainMiddleware):
    """
    Field is_active can be used to temporary disable tenant and
    block access to their site. Modifying get_tenant method from
    TenantMiddleware allows us to check if tenant should be available
    """
    def get_tenant(self, domain_model, hostname):
        tenant = super().get_tenant(domain_model, hostname)
        if not tenant.is_active:
            raise self.TENANT_NOT_FOUND_EXCEPTION("Tenant is inactive")
        return tenant
