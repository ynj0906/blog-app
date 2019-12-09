from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.test import Client


class TestMain(TestCase):
    fixtures = ["test_views.json"]
    #
    # @classmethod
    # def setUpClass(cls):
    #     #オーバーライドする場合は最初に、super().setUpClass()を呼び出す
    #     super().setUpClass()
    #     #TODO：下記で何らかの事前準備処理
    #
    #
    # @classmethod
    # def setUpTestData(cls):

    # def setUp(self):
    #     #テストケースで頻繁に使う情報を変数に格納
    #

    def test_get_context_data(self):
        # kwargs = {}
        # context = get_context_data(**kwargs)

        response = self.client.get('/contents/main')
        # self.assertEqual(200, response.status_code)
        print("あ")
        print(response.context[-1]['object_list'])

    def test_get(self):

        response = self.client.get('/contents/main',{"keyword": "編集"})
        # print(response)
        # print(response.context)

        self.assertIsNotNone(response.context['search_keyword'])




    # self.assertIsNone(request.Get.get("keyword"))

    # def get_context_data(self, **kwargs):
    # context = super(ListView, self).get_context_data(**kwargs)
    #
    #     print(1)
    #     if self.request.GET.get('keyword') is not None:  # アクセスしたURLにパラーメターがあれば分岐
    #         search_keyword = self.request.GET.get('keyword')
    #         context['search_keyword'] = search_keyword
    #         if search_keyword:
    #             article_list = Article.objects.filter(text__contains=search_keyword)
    #             context["article_list"] = article_list  # フィルタした結果を辞書型としてcontextに追加
    #             print(context)
    #             return context
    #     else:
    #         print(2)
    #         queryset = super(ListView, self).get_context_data(**kwargs)
    #         print(queryset)
    #         return queryset

    # def tearDown(self):
    #     #setUp()の後始末処理
    #     self.fp.close()
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     #TODO:　setUpClas()の後始末処理
    #     #オーバーライドする場合は最後に。super().tearDownClass()を呼び出す
    #     super().tearDownClass()
