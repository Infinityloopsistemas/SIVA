<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- FORM WIZARD
                    ================================================== -->
                    <!-- Form Wizard -->
                    <div class="callout callout-info">
                        <h4>jQuery Steps</h4>
                        <p>An all-in-one wizard plugin that is extremely flexible, compact and feature-rich. For more implementation, please <a rel="tooltip" title="jQuery Steps Documentation" target="_blank" href="https://github.com/rstaib/jquery-steps/wiki">Read Documentation</a></p>
                    </div>

                    <form data-form="wizard" data-validate="form" role="form" class="form-horizontal">
                        <div data-wizard>
                            <h3>Account</h3>
                            <section>
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="username">User name *</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver">@</span>
                                            <input class="form-control" id="username" name="username" type="text" minlength="2" required>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="passwd">Password *</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-rss"></i></span>
                                            <input class="form-control" id="passwd" name="passwd" type="password" minlength="2" required>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="confirm_passwd">Confirm Password *</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-rss"></i></span>
                                            <input class="form-control" id="confirm_passwd" name="confirm_passwd" type="password" equalTo="#passwd">
                                        </div>
                                    </div>
                                </div><!-- /form-group -->
                                <div class="clearfix"></div>
                            </section><!-- /step 1 -->

                            <h3>Profile</h3>
                            <section>
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="firstname">First name *</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-user"></i></span>
                                            <input class="form-control" id="firstname" name="firstname" type="text" required>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="lastname">Last name *</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-user"></i></span>
                                            <input class="form-control" id="lastname" name="lastname" type="text" required>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="email">Email *</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-envelope-o"></i></span>
                                            <input class="form-control" id="email" name="email" type="email" required>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="address">Address</label>
                                    <div class="col-sm-7">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-road"></i></span>
                                            <input class="form-control" id="address" name="address" type="text">
                                        </div>
                                    </div>
                                </div><!-- /form-group -->
                            </section><!-- /step 2 -->

                            <h3>Hints</h3>
                            <section>
                                <div class="alert alert-info">
                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum ab excepturi odio dicta asperiores id?</p>
                                </div>
                                <div class="alert alert-warning">
                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dignissimos, consequatur laborum maxime aperiam quis saepe!</p>
                                </div>
                                <div class="alert alert-danger">
                                    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque omnis porro nisi deserunt ipsum inventore.</p>
                                </div>
                            </section><!-- /step 3 -->

                            <h3>Finish</h3>
                            <section>
                                <div class="form-group">
                                    <div class="col-sm-offset-1 col-sm-7">
                                        <div class="nice-checkbox">
                                            <input class="checkbox-o" id="term" name="term" type="checkbox" required>
                                            <label for="term">
                                                I agree with the Terms and Conditions.
                                            </label>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->
                            </section><!-- /step 4 -->
                        </div><!-- /wizard -->
                    </form><!-- /form wizard -->