    my %config;
	my @order;
    open my $file, '<', 'default.ini' or die $!;
    while(<$file>) {
        chomp; 
		if(m/^#/) {
		  next;
		}
        (my $key, my $value) = split /=/, $_;
		$key =~ s/^\s+//;
		$key =~ s/\s+$//;
		$value =~ s/^\s+//;
		$value =~ s/\s+$//;
        $config{$key} = $value;
		push(@order, $key);
    }

print join " , ", 	@order, "\n";	
   foreach (@order) {
     print $_ , " has value : ", $config{$_}, "\n";
   }