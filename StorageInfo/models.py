from django.db import models


# Create your models here.

class Asset(models.Model):
    """   所有资产的共有数据表  """

    asset_type_choice = (
        ('storagedevice', '存储'),
        ('sanswitch', '光纤交换机'),
    )

    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '故障'),
        (3, '备用'),
        (4, '未知'),
    )

    asset_idc_choice = (
        ('nh11', '南汇1-1'),
        ('nh12', '南汇1-2'),
        ('nh21', '南汇2-1'),
        ('nh31', '南汇3-1'),
        ('zp', '周浦机房'),
        ('xj', '测试机房'),
        ('hf', '呼叫中心'),
    )
    asset_type = models.CharField(choices=asset_type_choice, max_length=64,
                                  verbose_name="资产类型")
    name = models.CharField(max_length=64, verbose_name="资产名称")
    sn = models.CharField(max_length=128, unique=True, verbose_name="资产序列号")
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name="设备状态")
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name="维保商",
                                     on_delete=models.SET_NULL)
    pinpai = models.CharField(max_length=64, null=True, blank=True, verbose_name="品牌")
    model = models.CharField(max_length=64, null=True, blank=True, verbose_name="型号")
    tags = models.CharField(max_length=64, verbose_name="资产标签")
    idc = models.CharField(choices=asset_idc_choice, max_length=64, default='nh11', verbose_name="机房")
    cabinet = models.CharField(max_length=64, null=True, blank=True, verbose_name="机柜位置")
    firmware = models.CharField(max_length=128, null=True, blank=True, verbose_name="固件版本")
    purchase_day = models.DateField(null=True, blank=True, verbose_name="维保开始时间")
    expire_day = models.DateField(null=True, blank=True, verbose_name="维保结束时间")
    mgt_ip = models.CharField(max_length=128, null=True, blank=True, verbose_name="管理地址")

    def __str__(self):
        return self.sn
    class Meta:
        verbose_name = "资产总表"
        verbose_name_plural = "资产总表"


class Manufacturer(models.Model):
    """厂商"""
    name = models.CharField('厂商名称', max_length=64, unique=True)
    telephone = models.CharField('支持电话', max_length=30, blank=True, null=True)
    memo = models.CharField('备注', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "维保厂商"
        verbose_name_plural = "维保厂商"


class StorageDevice(models.Model):
    """存储设备"""

    sub_asset_type_choice = (
        (0, '统一存储'),
        (1, 'SAN存储'),
        (2, 'NAS存储'),
        (3, '备份存储'),
    )
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="存储类型")
    vsp_ip = models.CharField(max_length=32, blank=True, null=True, verbose_name="VSP/管理机IP")
    nas_ip = models.CharField(max_length=64, blank=True, null=True, verbose_name="NAS_IP")
    memo = models.CharField('备注', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.asset.sn

    class Meta:
        verbose_name = "存储设备"
        verbose_name_plural = "存储设备"


class SanSwitch(models.Model):
    sub_asset_type_choice = (
        ('24port', '24口光纤交换机'),
        ('48port', '48口光纤交换机'),
        ('96port', '96口光纤交换机'),
    )
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    sub_asset_type = models.CharField(choices=sub_asset_type_choice, max_length=64, default='24port',
                                      verbose_name="光纤交换机类型")
    domain_id = models.CharField(max_length=12, null=True, blank=True, verbose_name="Domain_ID")

    def __str__(self):
        return self.asset.sn

    class Meta:
        verbose_name = "光纤交换机"
        verbose_name_plural = "光纤交换机"