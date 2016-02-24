 use Getopt::Long;
    use Pod::Usage;
    my $conf = 0;
    my $ini = 0;
    GetOptions('conf' => \$conf, ini => \$ini) ;
	
	print $conf , "\n";
	print $ini , "\n";
	print $opt_conf , "\n";
	print $opt_ini , "\n";
	
	print "conf", ${$conf};
	print "ini", ${$ini};
	
    __END__
    