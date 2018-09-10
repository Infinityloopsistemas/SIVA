<?php

if(!isset($_SERVER['HTTP_X_PJAX'])){

    $content = basename($_SERVER['SCRIPT_NAME']);

    $_SERVER['HTTP_X_PJAX'] = true;
    include 'stilearn.base.template.php';
    die();
}

?>
                    <!-- INVOICE
                    ====================== -->
                    <div class="invoice-wapper">
                        <div class="btn-group pull-right">
                            <a href="#" class="btn btn-default btn-sm"><i class="fa fa-print"></i> Print invoice</a>
                            <a href="#" class="btn btn-default btn-sm"><i class="fa fa-download"></i> Download invoice</a>
                        </div>
                        <div class="clearfix"></div>
                        <div class="page-header">
                            <div class="invoice-brand img-circle bordered border-2x border-cloud pull-right">
                                <img width="100px" height="100px" src="ico/favico-144-precomposed.png">
                            </div>
                            <h3>Invoice #742 <small>Update a template</small></h3>
                        </div><!--/page-header-->

                        <div class="row">
                            <div class="col-md-4">
                                <p class="text-muted"><strong>From</strong></p>
                                <p>Example Company</p>
                                <p>47 Address</p>
                                <p>Example, NY.80091</p>
                                <p>invoice@mail.com</p>
                            </div><!--/cols-->

                            <div class="col-md-4">
                                <p class="text-muted"><strong>To</strong></p>
                                <p>XYZ Corp</p>
                                <p>432 Main Street</p>
                                <p>San Francisco, CA 91234</p>
                            </div><!--/cols-->

                            <div class="col-md-4">
                                <p>Invoice No. 742</p>
                                <p>Invoice Date. January 10, 2014</p>
                                <p>Payment Due. January 17, 2014</p>
                            </div><!--/cols-->
                        </div><!--/row-->

                        <div class="invoice-table table-responsive">
                            <table class="table table-bordered invoice">
                                <thead>
                                    <tr>
                                        <th>ITEM DESCRIPTIONS</th>
                                        <th>QTY</th>
                                        <th>PRICE</th>
                                        <th>TOTAL PRICE</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Lorem Ipsum</td>
                                        <td class="right">5.0</td>
                                        <td class="right">$4.00</td>
                                        <td class="right">$20.00</td>
                                    </tr>
                                    <tr>
                                        <td>Nulla pellentesque</td>
                                        <td class="right">3.0</td>
                                        <td class="right">$5.00</td>
                                        <td class="right">$15.00</td>
                                    </tr>
                                    <tr>
                                        <td>Leo ornare lacinia</td>
                                        <td class="right">13.0</td>
                                        <td class="right">$2.00</td>
                                        <td class="right">$26.00</td>
                                    </tr>
                                    <tr>
                                        <td>Est arcu integer consectetuer</td>
                                        <td class="right">5.0</td>
                                        <td class="right">$5.00</td>
                                        <td class="right">$25.00</td>
                                    </tr>
                                </tbody>
                                <tfoot>
                                    <tr>
                                        <th colspan="4">Invoice Totals</th>
                                    </tr>
                                    <tr>
                                        <td colspan="3">Invoice Subtotal</td>
                                        <td class="right">$66.00</td>
                                    </tr>
                                    <tr>
                                        <td colspan="3">Invoice Discount</td>
                                        <td class="right">($4.00)</td>
                                    </tr>
                                    <tr>
                                        <td colspan="3">Sales Tax  (8.5%)</td>
                                        <td class="right">$5.61</td>
                                    </tr>
                                    <tr>
                                        <td colspan="3">Total Due</td>
                                        <td class="right">USD $67.61</td>
                                    </tr>
                                </tfoot>
                            </table>
                        </div><!--/invoice-table-->
                    </div><!--/invoice-wrapper-->