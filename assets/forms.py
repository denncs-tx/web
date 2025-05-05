from django.forms import ModelForm, Textarea

from assets.models import LibraryItem


class LibraryItemForm(ModelForm):
    class Meta:
        model = LibraryItem
        fields = '__all__'
        labels = {
            'max_ue_version': 'Max UE Version',
            'target_android': 'Android',
            'target_gearvr': 'Gear VR',
            'target_hololens2': 'HoloLens 2',
            'target_html5': 'HTML5',
            'target_ios': 'iOS',
            'target_linux': 'Linux',
            'target_mac': 'Mac',
            'target_nintendo_switch': 'Nintendo Switch',
            'target_oculus': 'Oculus',
            'target_ps4': 'PS4',
            'target_steamvr_htcvive': 'SteamVR / HTC Vive',
            'target_win32': 'Windows 32-bit',
            'target_windows': 'Windows',
            'target_xboxone': 'Xbox One',
        }
