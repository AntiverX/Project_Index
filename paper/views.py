from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from . import forms


def index(request):
    # TODO 文献检索库的主界面
    ...


@login_required
def upload(request):
    # TODO 文献上传页面
    ...


@method_decorator(login_required, name='dispatch')
class CreateView(View):
    """"""
    # TODO(2019年7月15日 10:56:58)@men: 添加文件上传
    def get(self, request):
        jpf = forms.JournalPaperForm()
        cpf = forms.ConferencePaperForm()
        tpf = forms.ThesisPaperForm()
        return render(request, 'paper/create.html',
                      {'jpf': jpf, 'cpf': cpf, 'tpf': tpf})

    def post(self, request):
        paper_type = request.POST.get('PaperType')

        # TODO(2019年7月15日 13:02:14)@men: 驱动表
        if paper_type == 'journal':
            paper_form = forms.JournalPaperForm(request.POST)
        elif paper_type == 'conference':
            paper_form = forms.ConferencePaperForm(request.POST)
        elif paper_type == 'thesis':
            paper_form = forms.ThesisPaperForm(request.POST)
        else:
            paper_form = None

        if paper_form and paper_form.is_valid():
            try:
                paper_form.save()
            except Exception as e:
                print('error occured @ saving paper : {0}'.format(e))
            else:
                print('paper saved')

        return redirect("/paper/create")


@login_required
def statistics(request):
    # TODO 显示平台的文献统计数据，画个饼状图显示各个组的文献占比，显示各个人的文献占比等等
    ...


class DetailView(View):
    """"""
    def get(self, request):
        pass

    def post(self, request):
        pass
