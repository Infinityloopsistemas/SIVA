<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- WIDGET TABS
                    ================================================== -->
                    <!-- Tabs -->
                    <div class="callout callout-info">
                        <h4>Togglable tabs</h4>
                        <p>Dynamic tab functionality to transition through panes of local content, even via dropdown menus.</p>
                        <p><strong>Good news!</strong> The Panel Tabs also support sortable.</p>
                    </div>


                    <div class="panel panel-default">
                        <div class="panel-body">
                            <ul class="nav nav-tabs">
                                <li class="active"><a href="#botabs1" data-toggle="tab">Default</a></li>
                                <li><a href="#botabs2" data-toggle="tab">Tabs</a></li>
                            </ul>
                            <div class="tab-content" style="padding-top:15px">
                                <div class="tab-pane fade in active" id="botabs1">
                                    <p>Raw denim you probably haven't heard of them jean shorts Austin. Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                    <p>Food truck fixie locavore, accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                </div>
                                <div class="tab-pane fade" id="botabs2">
                                    <p>Etsy mixtape wayfarers, ethical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                    <p>Trust fund seitan letterpress, keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                </div>
                            </div><!-- /tab-content -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel -->


                    <div class="row">
                        <div class="col-md-6" data-toggle="sortable-widget">
                            <div class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home1" data-toggle="tab">Home</a></li>
                                        <li><a href="#profile1" data-toggle="tab">Profile</a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Stilearning <i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent1" data-toggle="tab">@bent</a></li>
                                                <li><a href="#iin1" data-toggle="tab">@iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Basic Panel Tabs</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home1">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile1">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent1">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin1">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div class="panel panel-success sortable-widget-item">
                                <div class="panel-heading">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home2" data-toggle="tab">Home</a></li>
                                        <li><a href="#profile2" data-toggle="tab">Profile</a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Stilearning <i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent2" data-toggle="tab">@bent</a></li>
                                                <li><a href="#iin2" data-toggle="tab">@iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Context Succes</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home2">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile2">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent2">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin2">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div class="panel panel-warning sortable-widget-item">
                                <div class="panel-heading">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home3" data-toggle="tab">Home</a></li>
                                        <li><a href="#profile3" data-toggle="tab">Profile</a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Stilearning <i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent3" data-toggle="tab">@bent</a></li>
                                                <li><a href="#iin3" data-toggle="tab">@iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Context Warning</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home3">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile3">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent3">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin3">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div class="panel panel-default sortable-widget-item">
                                <div class="panel-heading bg-white">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a rel="tooltip-bottom" title="Home" href="#home4" data-toggle="tab"><i class="fa fa-home"></i></a></li>
                                        <li><a rel="tooltip-bottom" title="Profile" href="#profile4" data-toggle="tab"><i class="fa fa-user"></i></a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent4" data-toggle="tab"><i class="fa fa-male"></i>Bent</a></li>
                                                <li><a href="#iin4" data-toggle="tab"><i class="fa fa-female"></i>Iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Minimalize /w Icons</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home4">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile4">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent4">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin4">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div id="panel-tabfeatures1" class="panel panel-default">
                                <div class="panel-heading bg-white">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#apple1" data-toggle="tab"><i class="fa fa-apple"></i></a></li>
                                        <li><a href="#twitter1" data-toggle="tab"><i class="fa fa-twitter"></i></a></li>
                                        <li>
                                            <a href="#" rel="tooltip-bottom" data-refresh="#panel-tabfeatures1" title="refresh">
                                                <i class="fa fa-refresh"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#" rel="tooltip-bottom" data-expand="#panel-tabfeatures1" title="expand">
                                                <i class="fa fa-expand"></i>
                                            </a>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title">With Nice Scroll <small>Unsortable</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="apple1" style="height:200px;" data-toggle="niceScroll" data-scroll-wrapper=".scroll-wrapper" data-scroll-cursorcolor="#ecf0f1">
                                            <div class="scroll-wrapper">
                                                <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                                <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                                <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                                <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate reiciendis eius quas neque expedita autem nihil nesciunt quisquam. Facere, similique provident reprehenderit doloribus dolorum aspernatur eligendi perspiciatis expedita nemo odit dolorem minus molestias est vitae ipsum officia illo obcaecati sit alias veniam porro nam pariatur libero id commodi repellat fuga mollitia eos modi iste. Molestiae, quaerat, fugiat, itaque veritatis saepe voluptates eveniet aliquam voluptatem quo architecto laboriosam quod velit praesentium. Quasi, temporibus, similique, quas, fuga sit alias ea cupiditate nulla id asperiores unde tenetur reprehenderit labore molestiae incidunt repudiandae impedit itaque eos voluptates nam eaque dolorem magni consequatur quisquam ut!</p>
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="twitter1" style="height:200px;" data-toggle="niceScroll" data-scroll-wrapper=".scroll-wrapper" data-scroll-cursorcolor="#ecf0f1">
                                            <div class="scroll-wrapper">
                                                <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                                <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                                <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                                <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                            </div>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->

                                <!-- Table -->
                                <table class="tablesorter table table-hover">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>First Name</th>
                                            <th>Last Name</th>
                                            <th>Username</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>Mark</td>
                                            <td>Otto</td>
                                            <td>@mdo</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                            <td>Jacob</td>
                                            <td>Thornton</td>
                                            <td>@fat</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                            <td>Larry</td>
                                            <td>the Bird</td>
                                            <td>@twitter</td>
                                        </tr>
                                    </tbody>
                                    <tfoot>
                                        <tr>
                                            <th colspan="4" class="ts-pager form-horizontal">
                                                <button type="button" class="btn btn-default btn-sm first"><i class="icon-step-backward fa fa-angle-double-left"></i></button>
                                                <button type="button" class="btn btn-default btn-sm prev"><i class="icon-arrow-left fa fa-angle-left"></i></button>
                                                <span class="pagedisplay"></span> <!-- this can be any element, including an input -->
                                                <button type="button" class="btn btn-default btn-sm next"><i class="icon-arrow-right fa fa-angle-right"></i></button>
                                                <button type="button" class="btn btn-default btn-sm last"><i class="icon-step-forward fa fa-angle-double-right"></i></button>
                                                <select class="pagesize input-sm" title="Select page size">
                                                    <option value="5" selected>5</option>
                                                    <option value="10">10</option>
                                                    <option value="25">25</option>
                                                    <option value="50">50</option>
                                                </select>
                                                <select class="pagenum input-sm" title="Select page number"></select>
                                            </th>
                                        </tr>
                                    </tfoot>
                                </table><!-- /table -->
                            </div><!-- /panel-tabs -->
                        </div><!-- /cols -->



                        <div class="col-md-6" data-toggle="sortable-widget">
                            <div class="panel panel-primary sortable-widget-item">
                                <div class="panel-heading">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home5" data-toggle="tab">Home</a></li>
                                        <li><a href="#profile5" data-toggle="tab">Profile</a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Stilearning <i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent5" data-toggle="tab">@bent</a></li>
                                                <li><a href="#iin5" data-toggle="tab">@iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Context Primary</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home5">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile5">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent5">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin5">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div class="panel panel-info sortable-widget-item">
                                <div class="panel-heading">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home6" data-toggle="tab">Home</a></li>
                                        <li><a href="#profile6" data-toggle="tab">Profile</a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Stilearning <i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent6" data-toggle="tab">@bent</a></li>
                                                <li><a href="#iin6" data-toggle="tab">@iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Context Info</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home6">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile6">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent6">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin6">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div class="panel panel-danger sortable-widget-item">
                                <div class="panel-heading">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home7" data-toggle="tab">Home</a></li>
                                        <li><a href="#profile7" data-toggle="tab">Profile</a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Stilearning <i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent7" data-toggle="tab">@bent</a></li>
                                                <li><a href="#iin7" data-toggle="tab">@iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Context Danger</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home7">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile7">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent7">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin7">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div class="panel panel-primary border-inverse sortable-widget-item">
                                <div class="panel-heading bg-inverse">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#home8" data-toggle="tab"><i class="fa fa-home"></i></a></li>
                                        <li><a href="#profile8" data-toggle="tab"><i class="fa fa-user"></i></a></li>
                                        <li class="dropdown">
                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-angle-down"></i></a>
                                            <ul class="dropdown-menu animated flipInX pull-right">
                                                <li><a href="#bent8" data-toggle="tab"><i class="fa fa-male"></i>Bent</a></li>
                                                <li><a href="#iin8" data-toggle="tab"><i class="fa fa-female"></i>Iin</a></li>
                                            </ul>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Minimalize /w Inverse</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bg-inverse">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="home8">
                                            <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                            <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                        </div>
                                        <div class="tab-pane fade" id="profile8">
                                            <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                            <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                        </div>
                                        <div class="tab-pane fade" id="bent8">
                                            <p class="text-muted"><strong>Etsy mixtape wayfarers</strong></p>
                                            <p>Ehical wes anderson tofu before they sold out mcsweeney's organic lomo retro fanny pack lo-fi farm-to-table readymade. Messenger bag gentrify pitchfork tattooed craft beer, iphone skateboard locavore carles etsy salvia banksy hoodie helvetica. DIY synth PBR banksy irony. Leggings gentrify squid 8-bit cred pitchfork. Williamsburg banh mi whatever gluten-free, carles pitchfork biodiesel fixie etsy retro mlkshk vice blog. Scenester cred you probably haven't heard of them, vinyl craft beer blog stumptown. Pitchfork sustainable tofu synth chambray yr.</p>
                                        </div>
                                        <div class="tab-pane fade" id="iin8">
                                            <p class="text-muted"><strong>Trust fund seitan letterpress</strong></p>
                                            <p>Keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin. Cred vinyl keffiyeh DIY salvia PBR, banh mi before they sold out farm-to-table VHS viral locavore cosby sweater. Lomo wolf viral, mustache readymade thundercats keffiyeh craft beer marfa ethical. Wolf salvia freegan, sartorial keffiyeh echo park vegan.</p>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->
                            </div><!-- /panel-tabs -->



                            <div id="panel-tabfeatures2" class="panel panel-primary border-inverse sortable-widget-item">
                                <div class="panel-heading bg-inverse">
                                    <ul class="nav nav-tabs">
                                        <li class="active"><a href="#apple2" data-toggle="tab"><i class="fa fa-apple"></i></a></li>
                                        <li><a href="#twitter2" data-toggle="tab"><i class="fa fa-twitter"></i></a></li>
                                        <li>
                                            <a href="#" rel="tooltip-bottom" data-collapse="#panel-tabfeatures2" title="collapse">
                                                <i class="fa fa-caret-down"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#" rel="tooltip-bottom" data-close="#panel-tabfeatures2" title="close">
                                                <i class="fa fa-times"></i>
                                            </a>
                                        </li>
                                    </ul><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Inverse & Nice Scroll</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bg-inverse">
                                    <div class="tab-content">
                                        <div class="tab-pane fade in active" id="apple2" style="height:200px;" data-toggle="niceScroll" data-scroll-wrapper=".scroll-wrapper">
                                            <div class="scroll-wrapper">
                                                <p class="text-muted"><strong>Raw denim you probably haven't heard of them jean shorts Austin.</strong></p>
                                                <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                                <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                                <p>Nesciunt tofu stumptown aliqua, retro synth master cleanse. Mustache cliche tempor, williamsburg carles vegan helvetica. Reprehenderit butcher retro keffiyeh dreamcatcher synth. Cosby sweater eu banh mi, qui irure terry richardson ex squid. Aliquip placeat salvia cillum iphone. Seitan aliquip quis cardigan american apparel, butcher voluptate nisi qui.</p>
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="twitter2" style="height:200px;" data-toggle="niceScroll" data-scroll-wrapper=".scroll-wrapper">
                                            <div class="scroll-wrapper">
                                                <p class="text-muted"><strong>Food truck fixie locavore</strong></p>
                                                <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                                <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                                <p>Accusamus mcsweeney's marfa nulla single-origin coffee squid. Exercitation +1 labore velit, blog sartorial PBR leggings next level wes anderson artisan four loko farm-to-table craft beer twee. Qui photo booth letterpress, commodo enim craft beer mlkshk aliquip jean shorts ullamco ad vinyl cillum PBR. Homo nostrud organic, assumenda labore aesthetic magna delectus mollit. Keytar helvetica VHS salvia yr, vero magna velit sapiente labore stumptown. Vegan fanny pack odio cillum wes anderson 8-bit, sustainable jean shorts beard ut DIY ethical culpa terry richardson biodiesel. Art party scenester stumptown, tumblr butcher vero sint qui sapiente accusamus tattooed echo park.</p>
                                            </div>
                                        </div>
                                    </div><!--/tab-content-->
                                </div><!-- /panel-body -->

                                <!-- Table -->
                                <table class="table table-hover bg-inverse border-inverse">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>First Name</th>
                                            <th>Last Name</th>
                                            <th>Username</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>Mark</td>
                                            <td>Otto</td>
                                            <td>@mdo</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                            <td>Jacob</td>
                                            <td>Thornton</td>
                                            <td>@fat</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                            <td>Larry</td>
                                            <td>the Bird</td>
                                            <td>@twitter</td>
                                        </tr>
                                    </tbody>
                                </table><!-- /table -->
                            </div><!-- /panel-tabs -->
                        </div><!-- /cols -->
                    </div><!-- /row -->