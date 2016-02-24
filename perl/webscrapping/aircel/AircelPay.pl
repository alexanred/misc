
use WWW::Mechanize;
use Storable;

sub logf
{
   my $filename = shift;
   my $content = shift;

open (MYFILE, ">$filename");
print MYFILE $content;
close (MYFILE);
 
}

$url = 'http://www.aircel.com/AircelWar/appmanager/aircel/chennai?_nfpb=true&_pageLabel=pages_home';
$m = WWW::Mechanize->new();
print "Getting aricel for chennai ..."."\n";
$m->get($url);

$filename = $0.'hompage.html';
logf($filename, $m->content);

print "Clicking on online recharge \n";


$m->follow_link( url_regex => qr/online-recharge/i );

$c = $m->content;

$filename = $0.'onlinerechargepage.html';
logf($filename, $m->content);

print "Filling mobile number .. \n";

$m->form_name('pro_frm');
$m->field('cirid', 'CHE');
$m->field('mobtxt','9094564186');
$m->field('network', '3G');
$m->field('services', '3GD');
$m->click_button(name => 'btn_submit'); 

$filename = $0.'afterclickingrecharge.html';
logf($filename, $m->content);

print "Selecting the amount .. \n";
$m->form_name('pro_frm');
$m->field('prorad', '198');

$m->field('hideaction', 'submit');
$m->click_button(name => 'btn_submit'); 



$filename = $0.'afterAmountSelection.html';
logf($filename, $m->content);

$m->form_name('sms_frm');
$m->field('pgopt', 'netbanking');
$m->field('pgrad', 'billdesk');
$m->field('hidAction', '2');
$m->click_button(name => 'image');


$filename = $0.'autosubmitRedirect1.html';
logf($filename, $m->content);
$m->submit();
$filename = $0.'autosubmitRedirect2.html';
logf($filename, $m->content);
$m->submit();

$filename = $0.'billdeskpage.html';
logf($filename, $m->content);


$m->field('paymode', 'NETB');
$m->field('txtBankID1', 'HDF');
$m->field('txtItemCode', 'DIRECT');
$m->field('txtBankID', 'HDF');

$m->dump_forms();
$m->click_button(name => 'button'); 

$m->dump_headers();
print $m->response->header('Location')."It is";
print $m->response->code;
print "String response : \n".$m->response->as_string("\n");
$filename = $0.'billdesktohdfc.html';
logf($filename, $m->content);