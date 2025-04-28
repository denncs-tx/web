class AssetsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'assets':
            return 'assets'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'assets':
            return 'assets'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'assets' or
            obj2._meta.app_label == 'assets'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'assets':
            return db == 'assets'
        return None


class KjvhbRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'kjvhb':
            return 'kjvhb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'kjvhb':
            return 'kjvhb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'kjvhb' or
            obj2._meta.app_label == 'kjvhb'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'kjvhb':
            return db == 'kjvhb'
        return None
