def figsword(y)
	tenstowords=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen" ,"twenty","twenty-one","twenty-two","twenty-three","twenty-four","twenty-five" ]
	tos=y.to_s
	l=tos.length
	spec=tos[0]
	spec2=tos[1]
	xspec=spec.to_i
	xspec2=spec2.to_i
	sum1=xspec+xspec2
	if l==2
		tenstowords.each do|i|
			
			b=tenstowords.index(i)
			
			if xspec==1&&xspec2==b
					puts"#{i}"
				
			end		
		end

		

	end
end

def figword(y)

	wordstoten=["zero","one","two","three","four","five","six","seven","eight","nine"]
	
	puts"#{y}"
	wordstoten.each do |j|
			
			c=wordstoten.index(j)
			if y==c
				puts"#{j}"
				break
			else
				figsword(y)
				break

			end

	end
    

end

figword(18)
