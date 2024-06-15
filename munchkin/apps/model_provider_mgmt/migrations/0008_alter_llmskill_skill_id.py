# Generated by Django 4.2.7 on 2024-06-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_provider_mgmt', '0007_alter_llmskill_skill_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llmskill',
            name='skill_id',
            field=models.CharField(blank=True, choices=[('action_llm_fallback', '开放领域问答'), ('action_llm_jenkins_build_analysis', 'Jenkins构建异常分析'), ('action_llm_ticket_summary', '智能提单总结'), ('action_llm_code_review', '代码审查')], max_length=255, null=True, verbose_name='技能类型'),
        ),
    ]