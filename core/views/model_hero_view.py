from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from core.models.model import Model, ModelStatistic, ModelTag, ModelPopularTime
from core.models.hero import Hero
from core.models.footer import Footer, FooterSubcategory
from core.models.content import Content
from core.models.page import ModelPage
from django.shortcuts import get_object_or_404

class ModelHeroDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        url_tag = request.query_params.get('url_tag')
        nikname = request.query_params.get('nikname')

        if not all([url_tag, nikname]):
            return Response(
                {"error": "url_tag and name are required parameters"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Get Hero data
            hero = get_object_or_404(Hero, url_tag=url_tag)
            # Get Content data based on hero's name
            content = get_object_or_404(Content, name=hero.language)
            # Get ModelPage data based on URL tag
            model_page = get_object_or_404(ModelPage, tag=url_tag)

            hero_data = {
                'logo': content.logo,
                'logo_alt': content.logo_alt,
                'header_placeholder': content.header_placeholder,
                'legal_info': content.legal_info,
                'footer': [
                    {
                        'name': footer.name,
                        'subcategories': [
                            {
                                'name': subcategory.name,
                                'url': subcategory.url
                            } for subcategory in footer.subcategories.all()
                        ]
                    } for footer in hero.footer.all()
                ]
            }

            # Get Model data by nikname
            model = get_object_or_404(Model, nikname=nikname)
            model_data = {
                'nikname': model.nikname,
                'name': model.name,
                'about_model': model.about_model,
                'footer_button_url': model.footer_button_url,
                'sign_up_here_url': model.sign_up_here_url,
                'hero_url': model.hero_url,
                'last_updated': model.last_updated,
                'avatar': model.avatar,
                'statistics': [
                    {
                        'name': stat.name,
                        'value': stat.value
                    } for stat in model.statistics.all()
                ],
                'tags': [
                    {
                        'tag': tag.tag,
                        'tag_name': tag.tag_name
                    } for tag in model.tags.all()
                ],
                'popular_times': [
                    {
                        'day': time.day,
                        'time': time.time,
                        'rating': time.rating
                    } for time in model.popular_times.all()
                ]
            }

            # Add model page content
            model_page_data = {
                'home_name': model_page.home_name,
                'likes': model_page.likes,
                'hottest': model_page.hottest,
                'last_updated': model_page.last_updated,
                'status_online': model_page.status_online,
                'status_offline': model_page.status_offline,
                'check_schedule': model_page.check_schedule,
                'check_bio': model_page.check_bio,
                'herp_image': model_page.herp_image,
                'about_model': model_page.about_model,
                'model_statistics': model_page.model_statistics,
                'related_cams': model_page.related_cams,
                'sign_up_here': model_page.sign_up_here,
                'sign_up_description': model_page.sign_up_description,
                'popular_times': model_page.popular_times,
                'tags': model_page.tags,
                'monday': model_page.monday,
                'tuesday': model_page.tuesday,
                'wednesday': model_page.wednesday,
                'thursday': model_page.thursday,
                'friday': model_page.friday,
                'saturday': model_page.saturday,
                'sunday': model_page.sunday,
                'footer_button_title': model_page.footer_button_title,
                'footer_button': model_page.footer_button
            }

            return Response({
                'hero': hero_data,
                'model': model_data,
                'model_page': model_page_data
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) 