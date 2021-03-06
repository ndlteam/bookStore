from django.contrib import admin
from django.utils import timezone

from watch_buy.models import Cart, Goods, GoodsPic, Order, OrderGood


class GoodsPicInline(admin.TabularInline):
    model = GoodsPic
    extra = 0


class OrderGoodInline(admin.TabularInline):
    model = OrderGood
    extra = 0

    def get_queryset(self, request):
        return


class CartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['studentID', 'GoodID', 'Qty']})
    ]
    list_display = ['studentID', 'user_name', 'good_isbn', 'good_name', 'Qty']
    search_fields = ['studentID__studentID', 'studentID__name', 'GoodID__GoodName', 'GoodID__GoodAuthor',
                     'GoodID__GoodISBN', 'GoodID__Category', 'GoodID__GoodIntro']

    def user_name(self, obj):
        return obj.studentID.name

    def good_isbn(self, obj):
        return obj.GoodID.GoodISBN

    def good_name(self, obj):
        return obj.GoodID.GoodName

    user_name.short_description = '姓名'
    good_isbn.short_description = 'ISBN'
    good_name.short_description = '书籍名称'


class GoodsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本信息', {'fields': ['GoodName', 'Category', 'GoodPrice', 'GoodAuthor', 'GoodIntro',
                             'Publisher', 'Pages', 'PublishDate', 'PrintDate', 'Size', 'Edition']}),
        ('销售信息', {'fields': ['GoodRemain', 'GoodDiscount']}),
        ('其他', {'fields': ['Intro_pic']})
    ]
    list_display = ['GoodName', 'GoodAuthor', 'FormattedISBN', 'Category', 'GoodRemain', 'show_discount', 'show_new']
    inlines = [GoodsPicInline]
    actions = ['set_discount', 'unset_discount', 'set_new_item', 'unset_new_item']
    list_filter = [
        ('IsForSale', admin.BooleanFieldListFilter),
        ('IsNew', admin.BooleanFieldListFilter)
    ]
    search_fields = ['GoodName', 'GoodAuthor', 'GoodISBN', 'Category', 'GoodIntro']

    def set_discount(self, request, queryset):
        rows_updated = queryset.update(IsForSale=1)
        self.message_user(request, "成功打折{}个商品".format(rows_updated))

    def unset_discount(self, request, queryset):
        rows_updated1 = queryset.update(IsForSale=0)
        rows_updated2 = queryset.update(GoodDiscount=1)
        self.message_user(request, "{}个商品成功恢复原价".format(rows_updated1, rows_updated2))

    def set_new_item(self, request, queryset):
        rows_updated = queryset.update(IsNew=1)
        self.message_user(request, "{}个商品成功设置为新品".format(rows_updated))

    def unset_new_item(self, request, queryset):
        rows_updated = queryset.update(IsNew=0)
        self.message_user(request, "{}个商品成功取消新品".format(rows_updated))

    def show_discount(self, obj):
        if obj.IsForSale == 0:
            return '否'
        return '是'

    def show_new(self, obj):
        if obj.IsNew == 0:
            return '否'
        return '是'

    set_discount.short_description = '设置所选的商品为打折品'
    unset_discount.short_description = '设置所选的商品取消打折'
    set_new_item.short_description = '设置所选的商品为新品'
    unset_new_item.short_description = '设置所选的商品为非新品'
    show_discount.short_description = '是否打折'
    show_new.short_description = '是否新品'


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('订单信息', {'fields': ['orderdate', 'shipdate', 'user', 'Comment']}),
        ('收货人信息', {'fields': ['username', 'telephone', 'address', 'zipcode', 'qq']})
    ]
    list_display = ['orderid',
                    'username',
                    'address',
                    'orderdate',
                    'show_canceled',
                    'show_handle',
                    'show_ship',
                    'show_complete',
                    'show_cancel',
                    'show_return',
                    'Comment'
                    ]
    inlines = [OrderGoodInline]
    actions = ['set_cancel', 'set_canceled', 'set_complete', 'set_handle', 'set_return', 'set_ship',
               'unset_cancel', 'unset_canceled', 'unset_complete', 'unset_handle', 'unset_return', 'unset_ship']
    list_filter = [
        ('IsCancle', admin.BooleanFieldListFilter),
        ('IsHandled', admin.BooleanFieldListFilter),
        ('IsShipped', admin.BooleanFieldListFilter),
        ('IsCompleted', admin.BooleanFieldListFilter),
        ('IsCancled', admin.BooleanFieldListFilter),
        ('IsReturn', admin.BooleanFieldListFilter)
    ]
    search_fields = ['user__studentID', 'user__name', 'orderid', 'username', 'address', 'telephone', 'Comment']

    def show_cancel(self, obj):
        if obj.IsCancle == 0:
            return '否'
        return '是'

    def show_handle(self, obj):
        if obj.IsHandled == 0:
            return '否'
        return '是'

    def show_ship(self, obj):
        if obj.IsShipped == 0:
            return '否'
        return '是'

    def show_complete(self, obj):
        if obj.IsCompleted == 0:
            return '否'
        return '是'

    def show_canceled(self, obj):
        if obj.IsCancled == 0:
            return '否'
        return '是'

    def show_return(self, obj):
        if obj.IsReturn == 0:
            return '否'
        return '是'

    def set_canceled(self, request, queryset):
        rows_updated = queryset.update(IsCancled=1)
        self.message_user(request, "成功设置{}个订单已退款完成".format(rows_updated))

    def unset_canceled(self, request, queryset):
        rows_updated = queryset.update(IsCancled=0)
        self.message_user(request, "成功设置{}个订单为未退款完成".format(rows_updated))

    def set_handle(self, request, queryset):
        rows_updated = queryset.update(IsHandled=1)
        self.message_user(request, "成功设置{}个订单为已确认".format(rows_updated))

    def unset_handle(self, request, queryset):
        rows_updated = queryset.update(IsHandled=0)
        self.message_user(request, "成功设置{}个订单为未确认".format(rows_updated))

    def set_ship(self, request, queryset):
        rows_updated1 = queryset.update(IsShipped=1)
        rows_updated2 = queryset.update(shipdate=timezone.now())
        self.message_user(request, "成功设置{}个订单已发货".format(rows_updated1, rows_updated2))

    def unset_ship(self, request, queryset):
        rows_updated = queryset.update(IsShipped=0)
        self.message_user(request, "成功设置{}个订单为未发货".format(rows_updated))

    def set_complete(self, request, queryset):
        rows_updated = queryset.update(IsCompleted=1)
        self.message_user(request, "成功设置{}个订单已完成".format(rows_updated))

    def unset_complete(self, request, queryset):
        rows_updated = queryset.update(IsCompleted=0)
        self.message_user(request, "成功设置{}个订单为未完成".format(rows_updated))

    def set_cancel(self, request, queryset):
        rows_updated = queryset.update(IsCancle=1)
        self.message_user(request, "成功设置{}个订单为取消订单成功".format(rows_updated))

    def unset_cancel(self, request, queryset):
        rows_updated = queryset.update(IsCancle=0)
        self.message_user(request, "成功设置{}个订单为未取消订单".format(rows_updated))

    def set_return(self, request, queryset):
        rows_updated = queryset.update(IsReturn=1)
        self.message_user(request, "成功设置{}个订单已退货".format(rows_updated))

    def unset_return(self, request, queryset):
        rows_updated = queryset.update(IsReturn=0)
        self.message_user(request, "成功设置{}个订单为未退货".format(rows_updated))

    show_canceled.short_description = '是否完成退款'
    show_handle.short_description = '是否确认订单'
    show_ship.short_description = '是否发货'
    show_complete.short_description = '订单是否完成'
    show_cancel.short_description = '是否已取消订单'
    show_return.short_description = '是否要求退款'

    set_cancel.short_description = '设置所选的订单为已取消订单'
    set_canceled.short_description = '设置所选的订单为已退款'
    set_complete.short_description = '设置所选的订单为已完成'
    set_handle.short_description = '设置所选的订单为已确认'
    set_return.short_description = '设置所选的订单为已退货'
    set_ship.short_description = '设置所选的订单为已发货'

    unset_cancel.short_description = '设置所选的订单为未取消订单'
    unset_canceled.short_description = '设置所选的订单为未取消'
    unset_complete.short_description = '设置所选的订单为未完成'
    unset_handle.short_description = '设置所选的订单为未确认'
    unset_return.short_description = '设置所选的订单为未退货'
    unset_ship.short_description = '设置所选的订单为未发货'


admin.site.register(Cart, CartAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
