
use WWW::Mechanize;
use Storable;


my $value = '47710K_web';
@rns = split(/ /);


$url = 'https://www.irctc.co.in';
$m = WWW::Mechanize->new();
print "INFO : Getting irctc.co.in";
$m->get($url);

print "Setting username and passord and submitting .. ";
$m->form_name('LoginForm');
$m->field('userName','alexanred');
$m->field('password','wewillwin');
$m->click_button(name => 'button'); 

print "Clicking on history link ... ";
$m->follow_link( url_regex => qr/history/i );

print "Re entering password";
$m->form_name('LoginForm');
$m->field('password','wewillwin');
$m->click_button(name => 'Submit'); 

print "here is the history details";
$c = $m->content;

print $c;
# $c !~ s/[^[:ascii:]]//g;
#print $c;

