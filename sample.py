import imgkit


# imgkit.from_url('http://google.com', 'out.jpg')
# imgkit.from_file('/opt/odoo/odoo15/core/test_html_image/sample.html', 'out.jpg')
# imgkit.from_string('Hello!', 'out.jpg')


# options = {
#     'format': 'png',

#     'encoding': "UTF-8",
#     'custom-header' : [
#         ('Accept-Encoding', 'gzip')
#     ],
#     'cookie': [
#         ('cookie-name1', 'cookie-value1'),
#         ('cookie-name2', 'cookie-value2'),
#     ],
# }

html = """
<div class="container oe_form_field oe_form_field_html o_field_widget o_quick_editable usmh-html-style" name="reason" data-original-title="" title="" style="pointer-events: none;">
  <div class="o_readonly">
    <p>
      <br>
    </p>
    <ul class="o_checklist">
      <li class="o_checked" id="checklist-id-652113219662">チェックボックス①</li>
      <li class="o_checked" id="checklist-id-1487787348225">チェックボックス②</li>
      <li id="checklist-id-158403491297">Test 1</li>
      <li id="checklist-id-1595977471813">Test 3</li>
      <li id="checklist-id-1254026844504">test&nbsp;</li>
    </ul>
    <p>
      <img src="https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg">
      <br>
    </p>
    <p>
      <br>
    </p>
    <p>
      <a target="_blank" rel="noreferrer">標記の件につきまして、下記の通り稟議申請致します。</a>
    </p>
    <p>　　　　　　　　　　　記</p>
    <p>
      <b>1.主旨　・・・・・・・・</b>
    </p>
    <p>　〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇</p>
    <p>　〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇</p>
    <p>　〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇</p>
    <p>　〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇</p>
    <p>　〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇</p>
    <p>
      <br>
    </p>
    <p>
      <img class="img-fluid o_we_custom_image" src="https://t3.ftcdn.net/jpg/06/48/79/10/360_F_648791013_cQK30SdyiLrVQ96Bqn2MOkz4JmvgttGr.jpg?access_token=1a2f0b06-07f6-4c3a-9dae-7d97463ada43">
      <br>
    </p>
    <p>
      <br>
    </p>
    <p>
      <b>2.対象機器</b>
    </p>
    <p>　〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇</p>
    <p>
      <br>
    </p>
    <p>
      <b>3.支払概要</b>
    </p>
    <p>　（1）支払先　　：㈱〇〇〇〇〇〇</p>
    <p>　（2）支払額　　：9999円（税抜）</p>
    <p>　（3）支払日　　：0000年00月00日</p>
    <p>
      <br>
    </p>
    <p>
      <b>4．添付資料</b>
    </p>
    <p>　（1）〇〇〇〇〇〇</p>
    <p>　（2）〇〇〇〇〇〇</p>
    <p>　（3）〇〇〇〇〇〇</p>
    <p>　　　　　　　　　　　　　　　　　　　　　　　　　　　　&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 以上</p>
    <p>----------------------------------------------------------------------------------------------------------</p>
    <p>支払先　　：</p>
    <p>支払日　　：</p>
    <p>支払額　　：金額000,000円、消費税\00,000円、合計\000,000円</p>
    <p>支払方法　：</p>
    <ul class="o_checklist">
      <li id="checklist-id-1436837293150">Test 1</li>
    </ul>
    <p>
      <br>
    </p>
    <ul class="o_checklist">
      <li id="checklist-id-209899759878">Test 1</li>
      <li id="checklist-id-597743344763">Test 1</li>
    </ul>
    <p>
      <br>
    </p>
    <ul class="o_checklist">
      <li id="checklist-id-69430034605">Test 1</li>
      <li id="checklist-id-1684756032861">Test 1</li>
      <li id="checklist-id-1268680211482">Test 1</li>
      <li id="checklist-id-1570170862410">Test 1</li>
      <li id="checklist-id-1246668671171">Test 1</li>
      <li class="o_checked" id="checklist-id-1328258278960">Test 1</li>
      <li id="checklist-id-1315538609528">Test 1</li>
      <li id="checklist-id-956448699939">Test 1</li>
      <li class="o_checked" id="checklist-id-307849584132">Test 1</li>
      <ul class="o_checklist">
        <li class="o_checked" id="checklist-id-334631354239">Test 1</li>
        <li class="o_checked" id="checklist-id-100446777769">Test 1</li>
        <li class=" o_checked" id="checklist-id-177731188721">Test 1</li>
        <li class=" o_checked" id="checklist-id-2828640754">Test 1</li>
        <li class=" o_checked" id="checklist-id-271455193638">Test 1</li>
        <li class="o_checked" id="checklist-id-1565935007433">Test 1</li>
        <li class="o_checked" id="checklist-id-1523251629538">Test 1</li>
        <li class="o_checked" id="checklist-id-198562872823">Test 1</li>
        <li class="o_checked" id="checklist-id-1249781557268">Test 1</li>
        <li class=" o_checked" id="checklist-id-1605298955704">Test 1</li>
        <li class=" o_checked" id="checklist-id-697310425677">Test 1</li>
        <li class="o_checked" id="checklist-id-455680741554">Test 1</li>
        <li class=" o_checked" id="checklist-id-116484478920">Test 1</li>
        <li class=" o_checked" id="checklist-id-1514834260356">Test 1</li>
        <li id="checklist-id-1619735835831">Test 1</li>
      </ul>
      <li class=" o_checked" id="checklist-id-146550164725"> Test 2 test test&nbsp; </li>
      <ul class="o_checklist">
        <li class=" o_checked" id="checklist-id-575259546581">test 1111 44444444444444444444444444444444444444444455555555555555555555---------------------------------------------------</li>
      </ul>
      <li class=" o_checked" id="checklist-id-205060267711"> 2</li>
    </ul>
    <p>
      <br>
    </p>
  </div>
</div>
"""

# Multiple CSS files
css = ['/home/ubuntu/html2image/css/bootstrap.min.css', '/home/ubuntu/html2image/styles.css']
# imgkit.from_file('/home/ubuntu/html2image/index.html', 'out.png', css=css)
imgkit.from_string(html, 'image_out.png', css=css)

# imgkit.from_url('http://google.com', 'out.png', options=options)