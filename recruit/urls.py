from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^educationalqual$', views.educationalQual, name = 'educationalQual'),
    url(r'^experiencedetails$', views.experienceDetails, name = 'experienceDetails'),
    url(r'^academic/$', views.academic, name = 'academic'),
    url(r'academic/(?P<flag>[0-9]+)/$', views.academic, name = 'academic'),    
    url(r'^subject_ref/$',views.subject_ref,name='subject_ref'),
    # Main Annexures
    url(r'^academic/annexure_e12_main', views.annexure_e12_main, name = 'annexure_e12_main'),
    url(r'^academic/annexure_f_main', views.annexure_f_main, name = 'annexure_f_main'),
    url(r'^academic/annexure_g_main', views.annexure_g_main, name = 'annexure_g_main'),
    url(r'^academic/annexure_h_main', views.annexure_h_main, name = 'annexure_h_main'),
    url(r'^academic/annexure_i_main', views.annexure_i_main, name = 'annexure_i_main'),
    url(r'^academic/annexure_j_main', views.annexure_j_main, name = 'annexure_j_main'),
    url(r'^academic/annexure_k_main', views.annexure_k_main, name = 'annexure_k_main'),
    url(r'^academic/annexure_l_main', views.annexure_l_main, name = 'annexure_l_main'),
    url(r'^academic/annexure_m_main', views.annexure_m_main, name = 'annexure_m_main'),
    url(r'^academic/annexure_n_main', views.annexure_n_main, name = 'annexure_n_main'),
    url(r'^academic/annexure_o_main', views.annexure_o_main, name = 'annexure_o_main'),
    url(r'^academic/annexure_p_main', views.annexure_p_main, name = 'annexure_p_main'),
    url(r'^academic/annexure_q_main', views.annexure_q_main, name = 'annexure_q_main'),
    url(r'^academic/annexure_r_main', views.annexure_r_main, name = 'annexure_r_main'),
    url(r'^academic/annexure_s_main', views.annexure_s_main, name = 'annexure_s_main'),
    url(r'^academic/annexure_t_main', views.annexure_t_main, name = 'annexure_t_main'),
    url(r'^academic/annexure_u_main', views.annexure_u_main, name = 'annexure_u_main'),
    url(r'^academic/annexure_v_main', views.annexure_v_main, name = 'annexure_v_main'),
    url(r'^academic/annexure_w_main', views.annexure_w_main, name = 'annexure_w_main'),
    url(r'^academic/annexure_x_main', views.annexure_x_main, name = 'annexure_x_main'),
    url(r'^academic/annexure_y_main', views.annexure_y_main, name = 'annexure_y_main'),
    url(r'^academic/annexure_z_main', views.annexure_z_main, name = 'annexure_z_main'),

    # Annexures
    url(r'^academic/annexure_a', views.annexure_a, name = 'annexure_a'),
    url(r'^academic/annexure_b', views.annexure_b, name = 'annexure_b'),
    url(r'^academic/annexure_c', views.annexure_c, name = 'annexure_c'),
    url(r'^academic/annexure_d', views.annexure_d, name = 'annexure_d'),
    url(r'^academic/annexure_e_1', views.annexure_e_1, name = 'annexure_e_1'),
    url(r'^academic/annexure_e2', views.annexure_e2, name = 'annexure_e2'),
    url(r'^academic/annexure_f', views.annexure_f, name = 'annexure_f'),
    url(r'^academic/annexure_g', views.annexure_g, name = 'annexure_g'),
    url(r'^academic/annexure_h', views.annexure_h, name = 'annexure_h'),
    url(r'^academic/annexure_i', views.annexure_i, name = 'annexure_i'),
    url(r'^academic/annexure_j', views.annexure_j, name = 'annexure_j'),
    url(r'^academic/annexure_k', views.annexure_k, name = 'annexure_k'),
    url(r'^academic/annexure_l', views.annexure_l, name = 'annexure_l'),
    url(r'^academic/annexure_m', views.annexure_m, name = 'annexure_m'),
    url(r'^academic/annexure_n', views.annexure_n, name = 'annexure_n'),
    url(r'^academic/annexure_o', views.annexure_o, name = 'annexure_o'),
    url(r'^academic/annexure_p', views.annexure_p, name = 'annexure_p'),
    url(r'^academic/annexure_q', views.annexure_q, name = 'annexure_q'),
    url(r'^academic/annexure_r', views.annexure_r, name = 'annexure_r'),
    url(r'^academic/annexure_s', views.annexure_s, name = 'annexure_s'),
    url(r'^academic/annexure_t', views.annexure_t, name = 'annexure_t'),
    url(r'^academic/annexure_u', views.annexure_u, name = 'annexure_u'),
    url(r'^academic/annexure_v', views.annexure_v, name = 'annexure_v'),
    url(r'^academic/annexure_w1', views.annexure_w1, name = 'annexure_w1'),
    url(r'^academic/annexure_w2', views.annexure_w2, name = 'annexure_w2'),
    url(r'^academic/annexure_x', views.annexure_x, name = 'annexure_x'),
    url(r'^academic/annexure_y', views.annexure_y, name = 'annexure_y'),
    url(r'^academic/annexure_z', views.annexure_z, name = 'annexure_z'),

    url(r'^printSummary/$',views.printSummary,name='printSummary'),
    url(r'^notsubmitted/$',views.notsubmitted,name='notsubmitted'),
    url(r'^print_main_application', views.print_main_application, name = 'print_main_application'),
    url(r'^print_annexures', views.print_annexures, name = 'print_annexures'),
    url(r'^uploadPaper/(?P<papernum>[0-9]{1})/$',views.uploadPaper),
    url(r'^lockApplication/$',views.lockApplication,name='lockApplication'),
    url(r'^printAck/$',views.printAck,name='printAck'),
    url(r'^refresh/(?P<annexName>[a-z0-9_]+)/$',views.refresh),
    url(r'^uploadExpDoc/$',views.uploadExpDoc),
    url(r'^all_annexures/$',views.all_annexures),
    url(r'^clone/$',views.clone),
    url(r'^unlock/$',views.unlock),
    url(r'^faculty_login/$',views.fac_login),
    url(r'^faculty_admin/$',views.fac_admin),
    url(r'^save_h/(?P<appID>[0-9]+)/(?P<number>[0-9]+)/$',views.save_h),
    url(r'^save_i/(?P<appID>[0-9]+)/(?P<number>[0-9]+)/$',views.save_i),
    url(r'^save_h2/(?P<appID>[0-9]+)/(?P<number>[0-9]+)/$',views.save_h2),
    url(r'^save_i2/(?P<appID>[0-9]+)/(?P<number>[0-9]+)/$',views.save_i2),
    url(r'^faculty_admin/logout$',views.fac_logout),
    url(r'^applicant/(?P<appID>[0-9]+)/$',views.options3),
    url(r'viewappl/(?P<appID>[0-9]+)/$',views.viewappl),
    url(r'viewannex/(?P<appID>[0-9]+)/$',views.viewannex),
    url(r'viewscrutiny/(?P<appID>[0-9]+)/$',views.appSum),
    url(r'^acceptpayment/(?P<deptID>[0-9]+)/(?P<appID>[0-9]+)/$',views.acceptpayment),
    url(r'^rejectpayment/(?P<deptID>[0-9]+)/(?P<appID>[0-9]+)/$',views.rejectpayment),
    url(r'viewedu/(?P<appID>[0-9]+)/$', views.viewedu),
    url(r'rejectcandidate/(?P<appID>[0-9]+)/$', views.rejectcandidate),
    url(r'submitRemark/(?P<appID>[0-9]+)/$', views.submitRemark),
    url(r'payment_login/$',views.paymentLogin),
    url(r'payment/$',views.paymentVerify),
    url(r'payment/(?P<deptID>[0-9]+)/$',views.paymentVerify),
    url(r'payment/logout$',views.paymentlogout),
    # url(r'^automatePayment$',views.automatePayment),
    url(r'copyh/$',views.copypasteh),
    url(r'copyi/$',views.copypastei),
    url(r'stats/$',views.statistics),
    url(r'log1/$',views.log1),
    url(r'log2/$',views.log2),
    url(r'export_ext/$',views.export_ext),
    url(r'export_int/$',views.export_int),
    url(r'genpdf/$',views.generate_pdf),
    url(r'call_letter/$', views.call_letter),
    url(r'getAppids/$', views.getAppids),
    url(r'call_letter_admin/$', views.call_letter_admin),
    url(r'mailmsg/(?P<type_id>[0-9]+)/$', views.mailmsg_admin),
    url(r'call_letter_accept/$', views.call_letter_accept),
    url(r'print_cl/(?P<type_id>[0-9]+)/$', views.print_cl),
    url(r'gen_shortlist/(?P<dept_id>[0-9]+)/$', views.gen_shortlist),
    url(r'gen_shortlist_admin/$', views.gen_shortlist_admin),
    url(r'call_letter_blank/$',views.call_letter_blank),
    url(r'gen_dets/(?P<dept_id>[0-9]+)/$',views.gen_dets),
    url(r'pass_reset/$',views.pass_reset),

    # url(r'stats/(?P<deptID>[0-9]+)/$',views.statistics),
]