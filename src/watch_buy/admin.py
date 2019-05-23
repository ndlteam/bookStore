from django.contrib import admin

from watch_buy.models import Cart, Goods, GoodsPic, Order, OrderGood


class GoodsPicInline(admin.TabularInline):
    model = GoodsPic
    extra = 0


class OrderGoodInline(admin.TabularInline):
    model = OrderGood
    extra = 0


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['studentID', 'GoodID', 'Qty']})
    ]
    list_display = ['studentID', 'user_name', 'good_isbn', 'good_name', 'Qty']

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
        ('基本信息', {'fields': ['GoodISBN', 'GoodName', 'GoodPrice', 'GoodAuthor', 'GoodIntro']}),
        ('销售信息', {'fields': ['GoodRemain', 'GoodDiscount', 'IsForSale', 'IsNew']}),
        ('其他', {'fields': ['Intro_pic']})
    ]
    list_display = ['GoodName', 'GoodISBN', 'GoodRemain', 'show_discount', 'show_new']
    inlines = [GoodsPicInline]
    actions = ['set_discount', 'unset_discount', 'set_new_item', 'unset_new_item']

    def set_discount(self, request, queryset):
        rows_updated = queryset.update(IsForSale=1)
        self.message_user(request, "成功打折{}个商品".format(rows_updated))

    def unset_discount(self, request, queryset):
        rows_updated = queryset.update(IsForSale=0)
        self.message_user(request, "{}个商品成功恢复原价".format(rows_updated))

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

    admin.site.get_action('delete_selected').short_description = '删除所选的商品'
    set_discount.short_description = '设置所选的商品为打折品'
    unset_discount.short_description = '设置所选的商品取消打折'
    set_new_item.short_description = '设置所选的商品为新品'
    unset_new_item.short_description = '设置所选的商品为非新品'
    show_discount.short_description = '是否打折'
    show_new.short_description = '是否新品'


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('订单信息', {'fields': ['orderdate', 'shipdate', 'user', 'IsShipped', 'IsCancle', 'IsHandled', 'IsCancled']}),
        ('收货人信息', {'fields': ['username', 'telephone', 'address', 'zipcode', 'qq']})
    ]
    list_display = ['username', 'address', 'orderdate', 'show_is_shipped']
    inlines = [OrderGoodInline]

    def show_is_shipped(self, obj):
        if obj.IsShipped == 0:
            return '否'
        return '是'

    show_is_shipped.short_description = '是否发货'


admin.site.register(Cart, CartAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
