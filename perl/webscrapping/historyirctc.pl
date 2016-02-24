
use WWW::Mechanize;

sub logf
{
   my $filename = shift;
   my $content = shift;

open (MYFILE, ">$filename");
print MYFILE $content;
close (MYFILE);
 
}

$username = <>;
$password = <>;
chop $username;
chop $password;
$url = 'https://www.irctc.co.in';
$m = WWW::Mechanize->new();
print "INFO : Getting irctc.co.in"."\n";
$m->get($url);

$filename = $0.'loginpage.html';
logf($filename, $m->content);
print $filename."\n";
print "Setting username and passord and submitting .. "."\n";
$m->form_name('LoginForm');
$m->field('userName', $username);
$m->field('password',$password);
$m->click_button(name => 'button'); 

$filename = $0.'afterlogin.html';
logf($filename, $m->content);
print "Clicking on history link ... "."\n";
$m->follow_link( url_regex => qr/history/i );
$filename = $0.'histpassword.html';
logf($filename, $m->content);
print "Re entering password";
$m->form_name('LoginForm');
$m->field('password',$password);
$m->click_button(name => 'Submit'); 

print "here is the history details"."\n";
$filename = $0.'history.html';
logf($filename, $m->content);
