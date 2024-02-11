from django.forms import ModelForm, TextInput, inlineformset_factory

from nyuseu.models import MyBoard, MyBoardFeeds


class MyBoardForms(ModelForm):
    """
        Form to build his/her own board
    """
    class Meta:
        model = MyBoard
        fields = ('name',)
        exclude = ('id',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class MyBoardFeedsForms(ModelForm):
    """
        Form to add the feed on our board of our choice
    """
    class Meta:
        model = MyBoardFeeds
        fields = ('feeds',)
        exclude = ('name',)
        widgets = {
            'feeds': TextInput(attrs={'class': 'form-control'}),
        }


MyBoardFeedsFormset = inlineformset_factory(MyBoard,
                                            MyBoardFeeds,
                                            fields=('feeds',),
                                            extra=5,
                                            can_delete=True)
