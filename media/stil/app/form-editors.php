<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- EDITORS
                    ================================================== -->
                    <!-- Wysihtml5 -->
                    <textarea class="form-control" rows="10" name="wysihtml5-1" data-input="wysihtml5" placeholder="Enter text ..." style="margin-bottom:20px" data-color></textarea>
                    
                    <!-- Markdown -->
                    <textarea name="markdown1" data-input="markdown" rows="15">### Hello there 
How are you?

I have bellow task for you :

Select from this text...
Click the bold on THIS WORD and make THESE ONE italic
Link GOOGLE to google.com
Test to insert image (and try to tab after write the image description)
Test Preview
And ending here... Click "List"

Enjoy!</textarea>


                    <div class="page-header">
                        <h1 id="buttons">As Panel Content</h1>
                    </div>
                    <div id="panel-fileinput" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-fileinput" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-fileinput" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-fileinput" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-fileinput" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Bootstrap Wysihtml5</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form action="#" role="form">
                                <textarea class="form-control" rows="10" name="wysihtml5-2" data-input="wysihtml5" placeholder="Enter text ..." data-color></textarea>
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-fileinput -->


                     <div id="panel-markdown" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-markdown" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-markdown" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-markdown" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-markdown" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Bootstrap Markdown</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form action="#" role="form">
                                <textarea name="markdown2" data-input="markdown" rows="15">### Hello there 
How are you?

I have bellow task for you :

Select from this text...
Click the bold on THIS WORD and make THESE ONE italic
Link GOOGLE to google.com
Test to insert image (and try to tab after write the image description)
Test Preview
And ending here... Click "List"

Enjoy!</textarea>
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-markdown -->