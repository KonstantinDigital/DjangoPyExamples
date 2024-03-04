jQuery(function($){
   $(".phone").mask("+7 (999) 999-99-99");
});

if (document.getElementById('register-form')){
    let ArticleRincCnt = 1
    let ArticleScopusCnt = 1
    document.getElementById('id_public_rinc_0').setAttribute('onclick', 'hideFieldsPublicRincArticle(false)');
    document.getElementById('id_public_rinc_1').setAttribute('onclick', 'hideFieldsPublicRincArticle(true)');

    document.getElementById('hidden_fields_public_rinc_article_writer').style.display = 'none';
    document.getElementById('hidden_fields_public_rinc_article_title').style.display = 'none';
    document.getElementById('hidden_fields_public_rinc_article_btn').style.display = 'none';
    function hideFieldsPublicRincArticle(hide){
            document.getElementById('hidden_fields_public_rinc_article_writer').style.display = hide ? 'none' : 'flex';
            document.getElementById('hidden_fields_public_rinc_article_title').style.display = hide ? 'none' : 'flex';
            document.getElementById('hidden_fields_public_rinc_article_btn').style.display = hide ? 'none' : 'inline';
            if (document.getElementById('hidden_fields_public_rinc_article_writer').style.display == 'flex') {
                document.getElementById('id_public_rinc_article_writer').setAttribute('required', true);
                document.getElementById('id_public_rinc_article_writer').setAttribute('name', 'rinc_writer'+String(ArticleRincCnt));
            } else {
                document.getElementById('id_public_rinc_article_writer').removeAttribute('required');
            }
            if (document.getElementById('hidden_fields_public_rinc_article_title').style.display == 'flex') {
                document.getElementById('id_public_rinc_article_title').setAttribute('required', true);
                document.getElementById('id_public_rinc_article_title').setAttribute('name', 'rinc_title'+String(ArticleRincCnt));
            } else {
                document.getElementById('id_public_rinc_article_title').removeAttribute('required');
            }
    }

    document.getElementById('id_public_scopus_0').setAttribute('onclick', 'hideFieldsPublicScopusArticle(false)');
    document.getElementById('id_public_scopus_1').setAttribute('onclick', 'hideFieldsPublicScopusArticle(true)');

    document.getElementById('hidden_fields_public_scopus_article_writer').style.display = 'none';
    document.getElementById('hidden_fields_public_scopus_article_title').style.display = 'none';
    document.getElementById('hidden_fields_public_scopus_article_btn').style.display = 'none';
    function hideFieldsPublicScopusArticle(hide){
            document.getElementById('hidden_fields_public_scopus_article_writer').style.display = hide ? 'none' : 'flex';
            document.getElementById('hidden_fields_public_scopus_article_title').style.display = hide ? 'none' : 'flex';
            document.getElementById('hidden_fields_public_scopus_article_btn').style.display = hide ? 'none' : 'inline';
            if (document.getElementById('hidden_fields_public_scopus_article_writer').style.display == 'flex') {
                document.getElementById('id_public_scopus_article_writer').setAttribute('required', true);
                document.getElementById('id_public_scopus_article_writer').setAttribute('name', 'scopus_writer'+String(ArticleScopusCnt));
            } else {
                document.getElementById('id_public_scopus_article_writer').removeAttribute('required');
            }
            if (document.getElementById('hidden_fields_public_scopus_article_title').style.display == 'flex') {
                document.getElementById('id_public_scopus_article_title').setAttribute('required', true);
                document.getElementById('id_public_scopus_article_title').setAttribute('name', 'scopus_title'+String(ArticleScopusCnt));
            } else {
                document.getElementById('id_public_scopus_article_title').removeAttribute('required');
            }
    }

    document.getElementById('id_training_0').setAttribute('onclick', 'hideFieldsTrainingDetails(false)');
    document.getElementById('id_training_1').setAttribute('onclick', 'hideFieldsTrainingDetails(true)');

    document.getElementById('hidden_fields_training_details').style.display = 'none';
    function hideFieldsTrainingDetails(hide){
            document.getElementById('hidden_fields_training_details').style.display = hide ? 'none' : 'flex';
            if (document.getElementById('hidden_fields_training_details').style.display == 'flex') {
                document.getElementById('id_training_details').setAttribute('required', true);
            } else {
                document.getElementById('id_training_details').removeAttribute('required');
            }
    }

    function AddFioList(){
            $("#fio-list").append('<textarea class="form-control input-fio" rows="1" name="rinc_writer'+String(ArticleRincCnt)+'"></textarea>');
        };

    function AddFioListScopus(){
            $("#fio-list-scopus").append('<textarea class="form-control input-fio-scopus" rows="1" name="scopus_writer'+String(ArticleScopusCnt)+'"></textarea>');
        };

    jQuery(document).ready(function($){
        $('.add_article').click(function() {
            ArticleRincCnt += 1;
            $("#fio-list").removeAttr('id');
            $("#add-input").removeAttr('onclick');
            $("#add-input").removeAttr('id');
            $("#hidden_fields_public_rinc_article_writer").removeAttr('id');
            $("#id_public_rinc_article_writer").removeAttr('id');
            $("#hidden_fields_public_rinc_article_title").removeAttr('id');
            $("#id_public_rinc_article_title").removeAttr('id');
            $("#hidden_fields_public_rinc_article_btn").removeAttr('id');
            $("#id_public_rinc_0").removeAttr('onclick');
            $("#id_public_rinc_1").removeAttr('onclick');
            $("#rinc_article_div").append('<div class="input-group mb-4 text-left"><label class="input-group-text small-text text-wrap" style="width: 6rem;">ФИО автора</label><div class="col-9" id="fio-list"><textarea id="id_public_rinc_article_writer" class="form-control input-fio" rows="1"></textarea></div><input id="add-input" class="btn btn-outline-primary" type="button" onclick="AddFioList()" value="+" /></div><div class="input-group mb-4 text-left"><label class="input-group-text small-text text-wrap" style="width: 6rem;">Наименование статьи</label><textarea id="id_public_rinc_article_title" class="form-control" cols="40" rows="5"></textarea></div>');
            $("#id_public_rinc_article_writer").attr('name', 'rinc_writer'+String(ArticleRincCnt));
            $("#id_public_rinc_article_title").attr('name', 'rinc_title'+String(ArticleRincCnt));
        });
    });
    jQuery(document).ready(function($){
        $('.submit').click(function() {
            $("#register-form").append('<textarea name="article_rinc_count" hidden>'+ArticleRincCnt+'</textarea>');
            $("#register-form").append('<textarea name="article_scopus_count" hidden>'+ArticleScopusCnt+'</textarea>');
        });
    });

    jQuery(document).ready(function($){
        $('.add_article_scopus').click(function() {
            ArticleScopusCnt += 1;
            $("#fio-list-scopus").removeAttr('id');
            $("#add-input-scopus").removeAttr('onclick');
            $("#add-input-scopus").removeAttr('id');
            $("#hidden_fields_public_scopus_article_writer").removeAttr('id');
            $("#id_public_scopus_article_writer").removeAttr('id');
            $("#hidden_fields_public_scopus_article_title").removeAttr('id');
            $("#id_public_scopus_article_title").removeAttr('id');
            $("#hidden_fields_public_scopus_article_btn").removeAttr('id');
            $("#id_public_scopus_0").removeAttr('onclick');
            $("#id_public_scopus_1").removeAttr('onclick');
            $("#scopus_article_div").append('<div class="input-group mb-4 text-left"><label class="input-group-text small-text text-wrap" style="width: 6rem;">ФИО автора</label><div class="col-9" id="fio-list-scopus"><textarea id="id_public_scopus_article_writer" class="form-control input-fio-scopus" rows="1"></textarea></div><input id="add-input-scopus" class="btn btn-outline-primary" type="button" onclick="AddFioListScopus()" value="+" /></div><div class="input-group mb-4 text-left"><label class="input-group-text small-text text-wrap" style="width: 6rem;">Наименование статьи</label><textarea id="id_public_scopus_article_title" class="form-control" cols="40" rows="5"></textarea></div>');
            $("#id_public_scopus_article_writer").attr('name', 'scopus_writer'+String(ArticleScopusCnt));
            $("#id_public_scopus_article_title").attr('name', 'scopus_title'+String(ArticleScopusCnt));
        });
    });
}
