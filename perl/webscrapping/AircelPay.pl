
use WWW::Mechanize;
use Storable;


$url = 'http://www.aircel.com/AircelWar/appmanager/aircel/chennai?_nfpb=true&_pageLabel=pages_home';
$m = WWW::Mechanize->new();
print "Getting aricel for chennai ..."."\n";
$m->get($url);
open (MYFILE, '>>hompage.html');
print MYFILE $m->content;
close (MYFILE); 

print "Clicking on online recharge ";


$m->follow_link( url_regex => qr/online recharge/i );

$c = $m->content;
open (MYFILE, '>>onlinerechargepage.html');
print MYFILE $m->content;
close (MYFILE); 


$m->form_name('pro_frm');
$m->field('cirid', 'CHE');
$m->field('mobtxt','9094564186');
$m->field('cmbbox_brands', '3GD');
$m->click_button(name => 'button'); 
print $c;
# $c !~ s/[^[:ascii:]]//g;
#print $c;

