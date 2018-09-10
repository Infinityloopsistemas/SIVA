<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- BASIC FORM
                    ================================================== -->
                    <!-- BASIC FORM  -->
                    <div id="panel-basicform" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-basicform" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-basicform" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-basicform" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-basicform" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Input Fields</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form class="form-horizontal form-bordered" role="form">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="input">Text Input</label>
                                    <div class="col-sm-5">
                                        <input type="text" class="form-control" id="input" placeholder="Placeholder" />
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputDis">Text Disable</label>
                                    <div class="col-sm-5">
                                        <input type="text" class="form-control" id="inputDis" placeholder="Placeholder" disabled />
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputPass">Password Input</label>
                                    <div class="col-sm-5">
                                        <input type="password" class="form-control" id="inputPass" placeholder="Placeholder" />
                                        <span class="help-block">A longer block of help text that breaks onto a new line and may extend beyond one line.</span>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputSelect">Selects</label>
                                    <div class="col-sm-5">
                                        <select class="form-control" id="inputSelect">
                                            <option>- Select One -</option>
                                            <option>1</option>
                                            <option>2</option>
                                            <option>3</option>
                                            <option>4</option>
                                            <option>5</option>
                                        </select>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputMultiple">Multiple</label>
                                    <div class="col-sm-5">
                                        <select class="form-control" id="inputMultiple" multiple>
                                            <option>1</option>
                                            <option>2</option>
                                            <option>3</option>
                                            <option>4</option>
                                            <option>5</option>
                                        </select>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Static control</label>
                                    <div class="col-sm-5">
                                        <p class="form-control-static">email@example.com</p>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Radios</label>
                                    <div class="col-sm-5">
                                        <!-- Keep using .checkbox for radio, couse bootstrap .radio have any conflict with uniform .radio -->
                                        <div class="checkbox">
                                            <label>
                                                <input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked>
                                                Option one is this and that&mdash;be sure to include why it's great
                                            </label>
                                        </div>
                                        <div class="checkbox">
                                            <label>
                                                <input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
                                                Option two can be something else and selecting it will deselect option one
                                            </label>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Checkboxes</label>
                                    <div class="col-sm-5">
                                        <div class="checkbox">
                                            <label>
                                                <input type="checkbox" name="checkboxes" value="1" checked> Option one is this and that
                                            </label>
                                        </div>
                                        <div class="checkbox">
                                            <label>
                                                <input type="checkbox" name="checkboxes" value="2"> Be sure to include why it's great
                                            </label>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Inline checkboxes</label>
                                    <div class="col-sm-5">
                                        <label class="checkbox-inline">
                                            <input type="checkbox" id="inlineCheckbox1" value="option1" checked /> @bent
                                        </label>
                                        <label class="checkbox-inline">
                                            <input type="checkbox" id="inlineCheckbox2" value="option2" /> @Iin
                                        </label>
                                        <label class="checkbox-inline">
                                            <input type="checkbox" id="inlineCheckbox3" value="option3" /> @stilearningTwit
                                        </label>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputTextarea">Textarea</label>
                                    <div class="col-sm-5">
                                        <textarea rows="3" class="form-control" id="inputTextarea" placeholder="Placeholder"></textarea>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputAutogrow">Autogrow</label>
                                    <div class="col-sm-5">
                                        <textarea rows="3" class="form-control autogrow" id="inputAutogrow" placeholder="Type any line and I will auto grow"></textarea>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <div class="col-sm-offset-3 col-sm-5">
                                        <button type="submit" class="btn btn-default">Submit Form</button>
                                    </div>
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-basicform -->




                    <div id="panel-rpcdefault" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-rpcdefault" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-rpcdefault" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-rpcdefault" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-rpcdefault" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Replaced default style</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-offset-2 col-md-10">
                                            <p class="text-muted"><strong>Checkbox</strong></p>
                                            <p>Just give you a nice custom Checkbox style with pure CSS and Font Awesome. Activate it width <code>.nice-checkbox</code></p>
                                        </div>
                                        <div class="col-md-offset-2 col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-1" />
                                                <label for="checkbox-1">Checkbox</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-2" />
                                                <label for="checkbox-2"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-3" />
                                                <label for="checkbox-3"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-4" />
                                                <label for="checkbox-4"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-5" />
                                                <label for="checkbox-5"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-6" />
                                                <label for="checkbox-6"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-checked-1" checked />
                                                <label for="checkbox-checked-1">Normal</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-checked-2" checked />
                                                <label for="checkbox-checked-2"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-checked-3" checked />
                                                <label for="checkbox-checked-3"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-checked-4" checked />
                                                <label for="checkbox-checked-4"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-checked-5" checked />
                                                <label for="checkbox-checked-5"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-checked-6" checked />
                                                <label for="checkbox-checked-6"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-disabled-1" disabled />
                                                <label for="checkbox-disabled-1">Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-disabled-2" disabled />
                                                <label for="checkbox-disabled-2"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-disabled-3" disabled />
                                                <label for="checkbox-disabled-3"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-disabled-4" disabled />
                                                <label for="checkbox-disabled-4"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-disabled-5" disabled />
                                                <label for="checkbox-disabled-5"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-disabled-6" disabled />
                                                <label for="checkbox-disabled-6"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-both-1" checked disabled />
                                                <label for="checkbox-both-1">Checked - Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-both-2" checked disabled />
                                                <label for="checkbox-both-2"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-both-3" checked disabled />
                                                <label for="checkbox-both-3"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-both-4" checked disabled />
                                                <label for="checkbox-both-4"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-both-5" checked disabled />
                                                <label for="checkbox-both-5"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-both-6" checked disabled />
                                                <label for="checkbox-both-6"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->
                                    </div><!--/row-->
                                    <br>

                                    <div class="row">
                                        <div class="col-md-offset-2 col-md-10">
                                            <p class="text-muted"><strong>Optional style</strong></p>
                                            <p>Just add <code>.checkbox-o</code> to <code>input[type="checkbox"]</code> and you get other Checkbox style.</p>
                                        </div>
                                        <div class="col-md-offset-2 col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-1" />
                                                <label for="checkbox-o-1">Normal</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-2" />
                                                <label for="checkbox-o-2"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-3" />
                                                <label for="checkbox-o-3"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-4" />
                                                <label for="checkbox-o-4"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-5" />
                                                <label for="checkbox-o-5"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-6" />
                                                <label for="checkbox-o-6"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-1" checked />
                                                <label for="checkbox-o-checked-1">Checked</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-2" checked />
                                                <label for="checkbox-o-checked-2"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-3" checked />
                                                <label for="checkbox-o-checked-3"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-4" checked />
                                                <label for="checkbox-o-checked-4"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-5" checked />
                                                <label for="checkbox-o-checked-5"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-6" checked />
                                                <label for="checkbox-o-checked-6"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-1" disabled />
                                                <label for="checkbox-o-disabled-1">Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-2" disabled />
                                                <label for="checkbox-o-disabled-2"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-3" disabled />
                                                <label for="checkbox-o-disabled-3"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-4" disabled />
                                                <label for="checkbox-o-disabled-4"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-5" disabled />
                                                <label for="checkbox-o-disabled-5"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-6" disabled />
                                                <label for="checkbox-o-disabled-6"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-1" checked disabled />
                                                <label for="checkbox-o-both-1">Checked - Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-2" checked disabled />
                                                <label for="checkbox-o-both-2"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-3" checked disabled />
                                                <label for="checkbox-o-both-3"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-4" checked disabled />
                                                <label for="checkbox-o-both-4"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-5" checked disabled />
                                                <label for="checkbox-o-both-5"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-6" checked disabled />
                                                <label for="checkbox-o-both-6"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->
                                    </div><!--/row-->
                                    <br>

                                    <div class="row">
                                        <div class="col-md-offset-2 col-md-10">
                                            <p class="text-muted"><strong>Radio</strong> <code>.nice-radio</code></p>
                                        </div>
                                        <div class="col-md-offset-2 col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radio_1" id="radio-1" />
                                                <label for="radio-1">Normal</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radio_2" id="radio-2" />
                                                <label for="radio-2"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radio_3" id="radio-3" />
                                                <label for="radio-3"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radio_4" id="radio-4" />
                                                <label for="radio-4"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radio_5" id="radio-5" />
                                                <label for="radio-5"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radio_6" id="radio-6" />
                                                <label for="radio-6"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radio_1" id="radio-checked-1" checked />
                                                <label for="radio-checked-1">Checked</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radio_2" id="radio-checked-2" checked />
                                                <label for="radio-checked-2"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radio_3" id="radio-checked-3" checked />
                                                <label for="radio-checked-3"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radio_4" id="radio-checked-4" checked />
                                                <label for="radio-checked-4"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radio_5" id="radio-checked-5" checked />
                                                <label for="radio-checked-5"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radio_6" id="radio-checked-6" checked />
                                                <label for="radio-checked-6"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radiodis_1" id="radio-disabled-1" disabled />
                                                <label for="radio-disabled-1">Disabled</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radiodis_2" id="radio-disabled-2" disabled />
                                                <label for="radio-disabled-2"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radiodis_3" id="radio-disabled-3" disabled />
                                                <label for="radio-disabled-3"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radiodis_4" id="radio-disabled-4" disabled />
                                                <label for="radio-disabled-4"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radiodis_5" id="radio-disabled-5" disabled />
                                                <label for="radio-disabled-5"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radiodis_6" id="radio-disabled-6" disabled />
                                                <label for="radio-disabled-6"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radiodis_1" id="radio-both-1" checked disabled />
                                                <label for="radio-both-1">Checked - Disabled</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radiodis_2" id="radio-both-2" checked disabled />
                                                <label for="radio-both-2"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radiodis_3" id="radio-both-3" checked disabled />
                                                <label for="radio-both-3"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radiodis_4" id="radio-both-4" checked disabled />
                                                <label for="radio-both-4"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radiodis_5" id="radio-both-5" checked disabled />
                                                <label for="radio-both-5"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radiodis_6" id="radio-both-6" checked disabled />
                                                <label for="radio-both-6"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->
                                    </div><!--/row-->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-rpcdefault -->



                    
                    <div id="panel-inpgroup" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-inpgroup" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-inpgroup" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-inpgroup" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-inpgroup" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Input groups</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="leftaddon">Left Addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" id="leftaddon" placeholder="Username">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" placeholder="Username">
                                        </div><!-- /input-group-in -->
                                        <p class="helper-block text-muted"><small>Just add <code>.input-group-in</code> to any input group and you get a beautifull minimalis style.</small></p>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="rightaddon">Right Addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <input type="text" class="form-control" id="rightaddon">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="bothaddon">Both Addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">$</span>
                                            <input type="text" class="form-control" id="bothaddon">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">$</span>
                                            <input type="text" class="form-control">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="checkaddon">Checkbox addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <span class="nice-checkbox">
                                                    <input class="checkbox-o" type="checkbox" name="addoncheckbox" id="addoncheckbox1" checked>
                                                    <label for="addoncheckbox1"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="checkaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">
                                                <span class="nice-checkbox">
                                                    <input class="checkbox-o" type="checkbox" name="addoncheckbox" id="addoncheckbox2">
                                                    <label for="addoncheckbox2"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="checkaddon">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="radioaddon">Radio addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <span class="nice-radio text-primary">
                                                    <input type="radio" name="addonradio" id="addonradio1" checked>
                                                    <label for="addonradio1"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="radioaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">
                                                <span class="nice-radio text-primary">
                                                    <input type="radio" name="addonradio" id="addonradio2">
                                                    <label for="addonradio2"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="radioaddon">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="btnaddon">Button addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-btn">
                                                <button class="btn btn-inverse" type="button">Go!</button>
                                            </span>
                                            <input type="text" class="form-control" id="btnaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-btn">
                                                <button class="btn btn-inverse" type="button"><i class="fa fa-rocket"></i></button>
                                            </span>
                                            <input type="text" class="form-control">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="btnaddonright">Right button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <input type="text" class="form-control" id="btnaddonright">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button">Go!</button>
                                            </span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-search"></i></button>
                                            </span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="btnaddonboth">Both button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-paperclip"></i></button>
                                            </span>
                                            <input type="text" class="form-control" id="btnaddonboth">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-share"></i></button>
                                            </span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-paperclip"></i></button>
                                            </span>
                                            <input type="text" class="form-control">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-share"></i></button>
                                            </span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="dropaddon">Dropdown button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">Action <i class="fa fa-angle-down"></i></button>
                                                <ul class="dropdown-menu">
                                                    <li><a href="#">Action</a></li>
                                                    <li><a href="#">Another action</a></li>
                                                    <li><a href="#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="#">Separated link</a></li>
                                                </ul>
                                            </div><!-- /btn-group -->
                                            <input type="text" class="form-control" id="dropaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">Action <i class="fa fa-angle-down"></i></button>
                                                <ul class="dropdown-menu">
                                                    <li><a href="#">Action</a></li>
                                                    <li><a href="#">Another action</a></li>
                                                    <li><a href="#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="#">Separated link</a></li>
                                                </ul>
                                            </div><!-- /btn-group -->
                                            <input type="text" class="form-control">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="segmentaddon">Segmented button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <input type="text" class="form-control" id="segmentaddon">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-primary" tabindex="-1">Action</button>
                                                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" tabindex="-1">
                                                    <i class="fa fa-info"></i>
                                                </button>
                                                <ul class="dropdown-menu" role="menu">
                                                    <li><a href="#">Action</a></li>
                                                    <li><a href="#">Another action</a></li>
                                                    <li><a href="#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="#">Separated link</a></li>
                                                </ul>
                                            </div>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-primary" tabindex="-1"><i class="fa fa-paperclip"></i></button>
                                                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" tabindex="-1">
                                                    <i class="fa fa-share"></i>
                                                </button>
                                                <ul class="dropdown-menu" role="menu">
                                                    <li><a href="#">Action</a></li>
                                                    <li><a href="#">Another action</a></li>
                                                    <li><a href="#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="#">Separated link</a></li>
                                                </ul>
                                            </div>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-inpgroup -->




                    <div id="panel-ctrlstate" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-ctrlstate" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-ctrlstate" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-ctrlstate" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-ctrlstate" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Control states</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="disabledInput">Disabled input</label>
                                    <div class="col-md-5">
                                        <input class="form-control" id="disabledInput" type="text" placeholder="Disabled input here..." disabled>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="disabledSelect">Disabled select menu</label>
                                    <div class="col-md-5">
                                        <select id="disabledSelect" class="form-control text-muted" disabled>
                                            <option>Disabled select</option>
                                        </select>
                                        <div class="checkbox">
                                            <label>
                                                <input type="checkbox" disabled> <span class="text-muted">Can't check this</span>
                                            </label>
                                        </div>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-success">
                                    <label class="col-sm-3 control-label" for="inputSuccess">Input with success</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="inputSuccess">
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-warning">
                                    <label class="col-sm-3 control-label" for="inputWarning">Input with warning</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="inputWarning">
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-error">
                                    <label class="col-sm-3 control-label" for="inputError">Input with error</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="inputError">
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-success">
                                    <label class="col-sm-3 control-label" for="addonSucces">Success with addon</label>
                                    <div class="col-md-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" name="addonSucces">
                                        </div><!-- /input-group -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-warning">
                                    <label class="col-sm-3 control-label" for="addonWarning">Warning with addon</label>
                                    <div class="col-md-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" name="addonWarning">
                                        </div><!-- /input-group -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-error">
                                    <label class="col-sm-3 control-label" for="addonError">Error with addon</label>
                                    <div class="col-md-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" name="addonError">
                                        </div><!-- /input-group -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-success has-feedback">
                                    <label class="col-sm-3 control-label" for="iconsSuccess">Success with icons</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="iconsSuccess">
                                        <span class="glyphicon glyphicon-ok form-control-feedback"></span>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-warning has-feedback">
                                    <label class="col-sm-3 control-label" for="iconsWarning">Warning with icons</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="iconsWarning">
                                        <span class="glyphicon glyphicon-warning-sign form-control-feedback"></span>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-error has-feedback">
                                    <label class="col-sm-3 control-label" for="iconsError">Error with icons</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="iconsError">
                                        <span class="glyphicon glyphicon-remove form-control-feedback"></span>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-ctrlstate -->




                    <div id="panel-ctrlsize" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-ctrlsize" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-ctrlsize" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-ctrlsize" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-ctrlsize" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Control sizing</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputSizing">Input Sizing</label>
                                    <div class="col-md-5">
                                        <input id="inputSizing" class="form-control input-lg" type="text" placeholder=".input-lg"> <br>
                                        <input class="form-control" type="text" placeholder="Default input"> <br>
                                        <input class="form-control input-sm" type="text" placeholder=".input-sm"> <br>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="selectSizing">Select Sizing</label>
                                    <div class="col-md-5">
                                        <select id="selectSizing" class="form-control input-lg">
                                            <option>.input-lg</option>
                                        </select> <br>
                                        <select class="form-control">
                                            <option>Default input</option>
                                        </select> <br>
                                        <select class="form-control input-sm">
                                            <option>.input-sm</option>
                                        </select>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <p class="text-muted"><strong>Column sizing</strong></p>
                                    <div class="row">
                                        <div class="col-md-12">
                                            <input type="text" class="form-control" placeholder=".col-md-12">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <input type="text" class="form-control" placeholder=".col-md-6">
                                        </div>
                                        <div class="col-md-6">
                                            <input type="text" class="form-control" placeholder=".col-md-6">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-4">
                                            <input type="text" class="form-control" placeholder=".col-md-4">
                                        </div>
                                        <div class="col-md-4">
                                            <input type="text" class="form-control" placeholder=".col-md-4">
                                        </div>
                                        <div class="col-md-4">
                                            <input type="text" class="form-control" placeholder=".col-md-4">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-ctrlsize -->